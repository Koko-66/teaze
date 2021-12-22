"""Construct category"""
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Create category"""

    name = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Set pluaral name for Category"""
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories:manage_categories', kwargs={'id': self.id})