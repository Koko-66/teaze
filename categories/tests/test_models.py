"""Tests for category models"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from categories.models import Category
from datetime import datetime


class CategoryTestCase(TestCase):
    """Test Category model"""

    @classmethod
    def setUpTestData(cls):
        """Set up data for testing"""
        cls.user = User.objects.create_user(username='admin')
        cls.category = Category.objects.create(name='animals', author=cls.user)
        cls.category2 = Category.objects.create(name='trivia', author=cls.user)
        cls.category3 = Category.objects.create(name='books', author=cls.user)

    def test_category_name_created(self):
        """Test creation of category name"""
        self.assertEqual(self.category.name, 'animals')

    def test_category_author_created(self):
        """Test assginement of author for category"""
        self.assertEqual(self.category.author.username, 'admin')

    def test_category_updated_on(self):
        """Test assignment of updated_on date for category"""
        # formatted to date only, otherwise will never be equal
        current_time = datetime.now().date()
        self.category.updated_on = current_time
        self.assertEqual(self.category.updated_on, current_time)

    def test_ordering_method(self):
        """Test ordering method"""
        category_list = Category.objects.all()
        self.assertEqual(category_list[1].name, 'books')

    def test_str_method(self):
        """Test string method"""

        self.assertEqual(str(self.category), self.category.name)
        self.assertEqual(str(self.category2), self.category2.name)

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        url = reverse('categories:manage_categories')
        self.assertEqual(self.category.get_absolute_url(), url)
