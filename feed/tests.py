from django.test import TestCase
from django.urls import reverse


class MainFeedViewTests(TestCase):

    def test_content_of_instaclone_main_feed(self):
        """
        Main feed shows "This is the homepage!"
        """
        response = self.client.get(reverse('instaclone-main_feed'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the homepage!")
