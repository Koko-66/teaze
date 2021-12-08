# """Testing for models"""

# from django.test import TestCase
# from quiz.models import Category, Quiz, Question


# class CategoryTestCase(TestCase):
#     """Test creation of Category object"""

#     @classmethod
#     def setUpTestData(cls):
#         """Set up instance of Category for testing"""
#         cls.category = Category.objects.create(name='animals')
  
#     def test_category_name_created(self):
#         self.assertEqual(self.category.name, 'animals')


# class QuizQuestionTestCase(TestCase):
#     """Test creation of Qustion object"""

#     # @classmethod
#     # def setUpTestData(cls):
#     #     """Set up instance of Question for testing"""
#     #     cls.quiz = Quiz.objects.create(title='Something')
#     #     cls.question = Question.objects.create(body='else and nothing', category='New')
#     #     cls.quiz_question = QuizQuestion.objects.create()

#     # def test_QuizQuestion_string_value(self):
#     #     self.assertEqual(str(self.QuizQuestion), 'Something - else and nothing')
