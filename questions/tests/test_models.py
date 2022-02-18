"""Test for questions models"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from categories.models import Category
from questions.models import Question, Option
from quiz.models import Quiz
from datetime import datetime


class QuestionTestCase(TestCase):
    """Test Question object methods"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Question and Option for testing"""

        cls.user = User.objects.create_user(username='admin')
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz_id=1)
        cls.question2 = Question.objects.create(body='New question text 2',
                                                author=cls.user,
                                                quiz_id=1)
        cls.option = Option.objects.create(option='Test option 1',
                                           question=cls.question,
                                           author=cls.user, is_correct=True)
        cls.option2 = Option.objects.create(option='Test option 2',
                                            question=cls.question,
                                            author=cls.user, is_correct=True)
        cls.option3 = Option.objects.create(option='Test option 3',
                                            question=cls.question2,
                                            author=cls.user)
        cls.category = Category.objects.create(name='trivia', author=cls.user)
        cls.category2 = Category.objects.create(name='animals', author=cls.user)
        cls.quiz = Quiz.objects.create(title='New Quiz',
                                       category=cls.category)

    # test question methods
    def test_question_title_created(self):
        """Test creation of question name"""
        self.assertEqual(self.question.body, 'New question text')

    def test_question_author_created(self):
        """Test assginement of author for question"""
        self.assertEqual(self.question.author.username, 'admin')

    def test_question_updated_on(self):
        """Test assignment of updated_on date for question"""
        # formatted to date only, otherwise will never be equal
        current_time = datetime.now().date()
        self.question.updated_on = current_time
        self.assertEqual(self.question.updated_on, current_time)

    def test_question_str_method(self):
        """Test string method"""
        self.assertEqual(str(self.question), 'New question text')

    def test_get_options(self):
        """"Test getting options associated with the question."""
        options = self.question.get_options()
        self.assertEqual(len(options), 2)
    
    def test_get_categories(self):
        """Test getting a list of categories to display in templates."""
        categories = 'animals, trivia'
        self.question.category.add(self.category, self.category2)
        self.assertEqual(self.question.get_categories(), categories)
    
    def test_correct_options_count(self):
        """Test counter for correct options."""
        self.assertEqual(self.question.correct_options_count(), 2)

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        url = reverse('questions:question_details', kwargs={'pk': 1})
        self.assertEqual(self.question.get_absolute_url(), url)

    def test_ordering_method(self):
        """Test ordering method"""
        question_list = Question.objects.all()
        self.assertEquals(question_list[1].body, 'New question text')

    def test_option_str_method(self):
            """Test string method"""
            self.assertEqual(str(self.option), 'Test option 1')

