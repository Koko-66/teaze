"""Create question with answer options"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from quiz.models import Quiz, Category


STATUS = ((0, "Draft"), (1, "Approved"))


# Create your models here.
class Question(models.Model):
    """Create a question"""

    body = models.CharField(max_length=350, unique=True)
    category = models.ManyToManyField(Category,
                                      related_name='question')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='questions')
    # slug = models.SlugField(max_length=70, unique=True)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """Ordering for questions"""
        ordering = ['id']

    def __str__(self):
        return self.body

    def get_options(self):
        return self.options_set.all()


# Code adapted from:
# https://stackoverflow.com/questions/47867760/django-quiz-app-model-for-multiple-choice-questions#47867939
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options",
                                 on_delete=models.CASCADE)
    option = models.CharField("option", max_length=50)
    position = models.IntegerField("position")
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            # no duplicated option per question
            ("question", "option"),
            # no duplicated position per question
            ("question", "position")
        ]
        ordering = ["position"]
        verbose_name_plural = 'Answer options'

    def __str__(self):
        return self.option
