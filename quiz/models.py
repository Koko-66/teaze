from cloudinary.models import CloudinaryField
from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField


STATUS = ((0, "Draft"), (1, "Approved"))


class Category(models.Model):
    """Create category"""

    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Set pluaral name for Category"""
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Question(models.Model):
    """Create a question"""

    body = models.TextField(max_length=350, unique=True)
    # answers = ArrayField(
    #     models.CharField(max_length=200)
    # )
    # answers = models.
    # key = models.IntegerField(help_text='Correct answer')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='question')
    # slug = models.SlugField(max_length=70, unique=True)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """Ordering for questions"""
        ordering = ['id']

    def __str__(self):
        # return f'Question id: {self.question.id} / category: {self.category}'
        return self.body


# Code adapted from:
# https://stackoverflow.com/questions/47867760/django-quiz-app-model-for-multiple-choice-questions#47867939
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.PROTECT)
    option = models.CharField("option", max_length=50)
    position = models.IntegerField("position")
    is_correct = models.BooleanField(default=False)
    feedback_correct = models.CharField(max_length=200, default='You are correct!')
    feedback_incorrect = models.CharField(max_length=220, default='Sorry, you got this wrong.')

    class Meta:
        unique_together = [
            # no duplicated option per question
            ("question", "option"),
            # no duplicated position per question
            ("question", "position")
        ]
        ordering = ["position"]
        verbose_name_plural = 'Answer Options'

    def __str__(self):
        return self.option


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

    class Meta:
        verbose_name_plural = "Quizzes"

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