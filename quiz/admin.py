
"""Register Quiz with question as inline"""
from django.contrib import admin
from quiz.models import Quiz
from questions.models import Question


class QuestionInline(admin.TabularInline):
    model = Question

    list_filter = ('created_on', 'category')
    search_fields = ('name', 'email', 'body')


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# admin.site.register(Question)
admin.site.register(Quiz, QuizAdmin)
