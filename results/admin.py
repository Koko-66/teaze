"""Register 'resutls' models """
from django.contrib import admin
from results.models import Assessment, Answer


class AnswerInline(admin.TabularInline):
    """Show answers inline with Assessment in django admin."""
    model = Answer
    list_display = ['assessment']
    list_filter = ['assessment']


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    """Pull answers for the assessment inline in django admin."""
    inlines = [AnswerInline]
    list_display = [str, 'created_on', 'user', 'score']
    list_filter = ['quiz', 'user', 'score']


admin.site.register(Answer)
