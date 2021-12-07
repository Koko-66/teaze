from django.test import TestCase
from django.contrib.auth.models import User
from categories.models import Category


class CategoryTestCase(TestCase):
    """Test creation of Category object"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category for testing"""
        cls.user = User.objects.create_user(username='admin')
        cls.category = Category.objects.create(name='animals', author=cls.user)
  
    def test_category_name_created(self):
        """Test creation of category name"""
        self.assertEqual(self.category.name, 'animals')
    
    def test_category_author_created(self):
        """Test assginement of author for category"""
        self.assertEqual(self.category.author.username, 'admin')

    def test_str_method(self):
        """Test string method"""
        self.assertEqual(str(self.category), 'animals')
