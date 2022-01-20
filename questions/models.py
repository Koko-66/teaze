"""Question and answer options models with methods"""
from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from quiz.models import Quiz
from categories.models import Category


STATUS = ((0, "Draft"), (1, "Approved"))


class Question(models.Model):
    """Create a question"""

    body = models.CharField(max_length=350, unique=True)
    category = models.ManyToManyField(Category,
                                      related_name='question')
    quiz = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL,
                             related_name='questions')
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    feedback = models.CharField(max_length=200, blank=True)

    class Meta:
        """Ordering for questions"""
        ordering = ['id']

    def __str__(self):
        """Question string method"""
        return self.body

    def get_options(self):
        """"Get all options associated with the question."""
        return self.options.all()

    # code adapted from https://www.dev2qa.com/how-to-get-many-to-many-model-field-values-in-django-view/
    def get_categories(self):
        """Get list of categories to display in the template."""
        categories = ''

        for category in self.category.all():
            categories = categories + category.name + ', '
        return categories[:-2]

    def get_absolute_url(self):
        """Asbolute url for Qustion model."""
        return reverse('questions:question_detail', kwargs={'id': self.id})


# Code adapted from:
# https://stackoverflow.com/questions/47867760/django-quiz-app-model-for-multiple-choice-questions#47867939
class Option(models.Model):
    """Create Option object"""
    question = models.ForeignKey(Question, related_name="options",
                                 on_delete=models.CASCADE)
    option = models.CharField("option", max_length=50)
    position = models.IntegerField("position")
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Set meta data for the object: uniqueness, ordering and plural name
        """
        unique_together = [
            # no duplicated option per question
            ("question", "option"),
            # no duplicated position per question
            ("question", "position")
        ]
        ordering = ["position"]
        verbose_name_plural = 'Answer options'

    def __str__(self):
        """Option string method"""
        return self.option
