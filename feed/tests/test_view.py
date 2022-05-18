from django.test import RequestFactory
from django.urls import reverse
from feed import views


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
