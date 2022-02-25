"""Registration of models from 'questions' app"""

from django.contrib import admin
from questions.models import Option, Question


class OptionInline(admin.TabularInline):
    """Register option to show inline with question"""
    model = Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Register question"""
    inlines = [OptionInline]

    list_display = ('body', 'author', 'quiz', 'created_on')
    list_filter = ('category', 'quiz', 'created_on')
    search_fields = ['body']


admin.site.register(Option)
