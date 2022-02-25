
"""Settings for Django admin page"""

from django.contrib import admin
from quiz.models import Quiz
from questions.models import Question


class QuestionInline(admin.TabularInline):
    """Set question settings, with question as inline"""
    model = Question

    list_filter = ('created_on', 'category')
    search_fields = ('name', 'email', 'body')


class QuizAdmin(admin.ModelAdmin):
    """View settings for quiz"""
    inlines = [QuestionInline]
    prepopulated_fields = {"slug": ("title",)}


# admin.site.register(Question)
admin.site.register(Quiz, QuizAdmin)
