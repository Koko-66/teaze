from django.contrib import admin
from results.models import Assessment, Answer


class AnswerInline(admin.TabularInline):
    """Show answers inline with Assessment in django admin."""
    model = Answer
    # prepopulated_fields = {"answer": ("answer",)}
    list_filter = ('created_on', 'category')
    search_fields = ('category')


class AssessmentAdmin(admin.ModelAdmin):
    """Pull answers for the assessment inline in django admin."""
    inlines = [AnswerInline]
    list_display = (str, 'created_on')


admin.site.register(Assessment, AssessmentAdmin)

