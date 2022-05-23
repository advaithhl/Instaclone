import logging

import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from feed import views
from feed.models import Post
from mixer.backend.django import mixer

from utils import random_string

logger = logging.getLogger(__name__)


class TestRedirectToFeedView:
    def test_view_empty(self):
        request = RequestFactory().get(reverse('instaclone-view_empty'))
        response = views.redirect_to_feed(request)
        assert response.status_code == 302

    def test_edit_empty(self):
        request = RequestFactory().get(reverse('instaclone-edit_empty'))
        response = views.redirect_to_feed(request)
        assert response.status_code == 302

    def test_delete_empty(self):
        request = RequestFactory().get(reverse('instaclone-delete_empty'))
        response = views.redirect_to_feed(request)
        assert response.status_code == 302


@pytest.mark.django_db
class TestMainFeedView:
    def test_anonymous(self):
        request = RequestFactory().get(reverse('instaclone-main_feed'))
        request.user = AnonymousUser()
        response = views.main_feed(request)
        logger.info(f'Redirect URL is {response.url}')
        assert response.status_code == 302
        assert response.url == f'{reverse(settings.LOGIN_URL)}?next={reverse(settings.LOGIN_REDIRECT_URL)}'

    def test_main_feed(self):
        request = RequestFactory().get(reverse('instaclone-main_feed'))
        request.user = mixer.blend(User)
        logger.info(f'Mixer created user is {request.user}')
        logger.debug(f'All users queryset is {User.objects.all()}')
        response = views.main_feed(request)
        assert response.status_code == 200


@pytest.mark.django_db
class TestCreatePostView:
    def test_anonymous(self):
        request = RequestFactory().get(reverse('instaclone-create_post_view'))
        request.user = AnonymousUser()
        response = views.create_post_view(request)
        logger.info(f'Redirect URL is {response.url}')
        assert response.status_code == 302
        assert response.url == f'{reverse(settings.LOGIN_URL)}?next={reverse("instaclone-create_post_view")}'

    def test_get(self):
        request = RequestFactory().get(reverse('instaclone-create_post_view'))
        request.user = mixer.blend(User)
        logger.info(f'Mixer created user is {request.user}')
        logger.debug(f'All users queryset is {User.objects.all()}')
        response = views.create_post_view(request)
        assert response.status_code == 200
        assert b'form' in response.content

    def test_post(self, default_image):
        caption = random_string(512)
        data = {
            'content': default_image,
            'caption': caption
        }
        request = RequestFactory().post(reverse('instaclone-create_post_view'), data=data)
        request.user = mixer.blend(User)
        logger.info(f'Mixer created user is {request.user}')
        logger.debug(f'All users queryset is {User.objects.all()}')
        response = views.create_post_view(request)
        assert response.status_code == 302
        assert response.url == f'{reverse("instaclone-post_view", kwargs={"pk": 1})}'
        assert Post.objects.count() == 1
        created_post = Post.objects.first()
        logger.info(f'Currently created post is {created_post}')
        logger.debug(f'All posts queryset is {Post.objects.all()}')
        assert created_post.creator == request.user
        assert created_post.caption == caption
        assert created_post.liked_users.all().count() == 0

    def test_horizontal_picture(self, horizontal_image):
        caption = random_string(512)
        data = {
            'content': horizontal_image,
            'caption': caption
        }
        request = RequestFactory().post(reverse('instaclone-create_post_view'), data=data)
        request.user = mixer.blend(User)
        logger.info(f'Mixer created user is {request.user}')
        logger.debug(f'All users queryset is {User.objects.all()}')
        response = views.create_post_view(request)
        assert response.status_code == 302
        assert response.url == f'{reverse("instaclone-post_view", kwargs={"pk": 1})}'
        assert Post.objects.count() == 1
        created_post = Post.objects.first()
        logger.info(f'Currently created post is {created_post}')
        logger.debug(f'All posts queryset is {Post.objects.all()}')
        assert created_post.creator == request.user
        assert created_post.caption == caption
        assert created_post.liked_users.all().count() == 0

    def test_vertical_picture(self, vertical_image):
        caption = random_string(512)
        data = {
            'content': vertical_image,
            'caption': caption
        }
        request = RequestFactory().post(reverse('instaclone-create_post_view'), data=data)
        request.user = mixer.blend(User)
        logger.info(f'Mixer created user is {request.user}')
        logger.debug(f'All users queryset is {User.objects.all()}')
        response = views.create_post_view(request)
        assert response.status_code == 302
        assert response.url == f'{reverse("instaclone-post_view", kwargs={"pk": 1})}'
        assert Post.objects.count() == 1
        created_post = Post.objects.first()
        logger.info(f'Currently created post is {created_post}')
        logger.debug(f'All posts queryset is {Post.objects.all()}')
        assert created_post.creator == request.user
        assert created_post.caption == caption
        assert created_post.liked_users.all().count() == 0
