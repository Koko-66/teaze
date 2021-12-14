"""Quiz model and methods"""

from cloudinary.models import CloudinaryField
from django.db import models
from categories.models import Category


STATUS = ((0, 'Draft'), (1, 'Published'))


class Quiz(models.Model):
    """Create Quiz object"""

    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='quiz')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """Set plural name to show in admin"""
        verbose_name_plural = "Quizzes"

    def get_questions(self):
        """Get all questions assigned to thie quiz"""
        return self.questions.all()

    def __str__(self):
        """Quiz string method"""
        return self.title
