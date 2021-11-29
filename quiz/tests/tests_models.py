""" Module tests """
from django.test import TestCase
from quiz.models import Category


class CategoryTestCase(TestCase):
    """Tests for Category"""

    @classmethod
    def setUpTestData(self):
        """Set up instance of Category for testing"""
        self.category = Category.objects.create(name='animals')

    def test_category_name(self):
        self.assertEqual(self.category.name, 'animals')


# class QuestionTestCase(TestCase):
#     """Tests for Question model"""

#     @classmethod
#     def setUpTestData(cls):
#         """Set up instance of Question for testing"""
#         question = Question.ob