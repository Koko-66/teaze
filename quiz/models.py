# from cloudinary.models import CloudinaryField
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
