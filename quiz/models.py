"""Quiz model and methods"""
from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from categories.models import Category
# import random


STATUS = ((0, 'Draft'), (1, 'Published'))


class Quiz(models.Model):
    """Create Quiz object"""

    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='quiz')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=300, blank=True)
    # number_of_questions = models.IntegerField()
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
        # Randomisation of quesitons taken from Pyplane tutorial:
        # https://www.youtube.com/watch?v=T9xOjVJI1rg
        # questions = list(self.questions.all())
        # random.shuffle(questions)
        # return questions[:self.num_of_questions]
        return self.questions.all()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        """Quiz string method"""
        return self.title

    def get_absolute_url(self):
        """Get absolute url"""
        return reverse('quiz:quiz_details', kwargs={"slug": self.slug})
