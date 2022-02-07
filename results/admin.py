from django.contrib import admin
from results.models import Assessment, Answer

@admin.register(Answer)
class AnswerInline(admin.ModelAdmin):
    """Show answers inline with Assessment in django admin."""
    list_display = ['assessment']
    list_filter = ['assessment']
    # search_fields = ('name', 'email', 'body')
    

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    """Pull answers for the assessment inline in django admin."""
    list_display = [str, 'id', 'created_on', 'user']

# admin.site.register(Assessment, AssessmentAdmin)

