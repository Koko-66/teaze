"""Data models"""

from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


STATUS = ((0, "Draft"), (1, "Approved"))


class Category(models.Model):
    """Create category"""

    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Create a question"""

    body = models.CharField(max_length=250, unique=True)
    answers = ArrayField(
        models.CharField(max_length=200)
    )
    key = models.IntegerField(help_text='Correct answer')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='question')
    slug = models.SlugField(max_length=70, unique=True)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    feedback_correct = models.CharField(max_length=200)
    feedback_incorrect = models.CharField(max_length=220)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """Ordering for questions"""
        ordering = ['category']

    def __str__(self):
        # return f'Question id: {self.question.id} / category: {self.category}'
        return f'{self.slug} - {self.category}'


class Quiz(models.Model):
    """Create a quiz"""

    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='quiz')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    """Create quiz_question link"""

    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT,
                             related_name='quiz_question')
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.quiz)} - {str(self.question)}'


class Assessment(models.Model):
    """Crate assessment"""

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='assessment')
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quiz}-{self.user}'


class Answers(models.Model):
    """Create user answer"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answered_question')
    answer = models.IntegerField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE,
                                   related_name='answers')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.assessment}-{self.question}-{self.answer}'
