"""Tests for forms in categories app."""
from django.test import TestCase
from django.contrib.auth.models import User


class CategoryTestCase(TestCase):
    """Test Category form"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category for testing"""
        cls.user = User.objects.create_user(username='admin',
                                            password='password')

    def test_new_category_form(self):
        """Test override save method."""
        self.client.login(username='admin', password='password')
        data = {
            "name": "movies",
        }
        response = self.client.post('/categories/add_new_category/', data=data)
        self.assertRedirects(response, '/categories/')
