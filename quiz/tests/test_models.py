"""Testing for models"""

from django.test import TestCase
from quiz.models import Category


class CategoryTestCase(TestCase):
    """Tests for Category"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category for testing"""
        cls.category = Category.objects.create(name='animals')
    
    def test_category_name_created(self):
        self.assertEqual(self.category.name, 'animals')
