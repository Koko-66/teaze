from cloudinary.models import CloudinaryField
from django.db import models
# from django.contrib.auth.models import User
from categories.models import Category
# from django.contrib.postgres.fields import ArrayField
# from django.core.validators import MaxValueValidator, MinValueValidator


class Quiz(models.Model):
    """Create a quiz"""

    title = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(Category,
                                      related_name='quiz')
    # slug = models.SlugField(max_length=200, unique=True)
    prepopulated_fields = {"slug": ("title",)}
    description = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.questions_set.all()


