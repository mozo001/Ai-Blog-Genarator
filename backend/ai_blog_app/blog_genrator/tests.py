from django.test import SimpleTestCase
from django.urls import reverse


class BlogGeneratorViewsTests(SimpleTestCase):
    def test_index_page_renders(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_renders(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_renders(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
