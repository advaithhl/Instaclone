import logging

import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from feed import views
from mixer.backend.django import mixer

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
        logging.info(f'Redirect URL is {response.url}')
        assert response.status_code == 302
        assert response.url == f'{reverse(settings.LOGIN_URL)}?next={reverse(settings.LOGIN_REDIRECT_URL)}'

    def test_main_feed(self):
        request = RequestFactory().get(reverse('instaclone-main_feed'))
        request.user = mixer.blend(User)
        logger.info(f'Mixer created user is {request.user}')
        logger.debug(f'All users queryset is {User.objects.all()}')
        response = views.main_feed(request)
        assert response.status_code == 200
