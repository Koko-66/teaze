# """Tests for results views"""
# from django.test import TestCase
# from .views import results


# class ResultsFunctionTestCase(TestCase):
#     """Test methods of Assessment and Answer objects"""

#     @classmethod
#     def setUpTestData(cls):
#         """Set up instance of Assessment and Answer for testing"""
#         cls.user = User.objects.create_user(username='user')
#         cls.category = Category.objects.create(name='Test', author=cls.user)
#         cls.quiz = Quiz.objects.create(title='Test Quiz', category=cls.category)
#         cls.question = Question.objects.create(body='New question text',
#                                                author=cls.user,
#                                                quiz_id=cls.quiz.pk)
#         cls.assessment = Assessment.objects.create(user=cls.user, quiz=cls.quiz, score=8)
#         cls.answer = Answer.objects.create(question=cls.question, answer=2, assessment=cls.assessment, )
