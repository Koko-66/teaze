"""Register category model in django admin"""
from django.contrib import admin
from categories.models import Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Register category and set items to show in admin"""
    list_display = ('name', 'author', 'created_on')
