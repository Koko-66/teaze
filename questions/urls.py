"""Urls for questions app"""
from django.urls import path
from .views import (
    AddQuestionView,
    add_question_view,
    # AddOptionView,
    add_option_view,
    QuestionDetailsView,
    EditQuestionView,
    DeleteQuestionView,
    # question_delete_view,
    QuestionListView,
    toggle_status,
)

app_name = 'questions'

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='manage_questions'),
    path('questions/add_question/', AddQuestionView.as_view(), name='add_question'),
    path('<slug:slug>/add_question/', add_question_view, name='add_question_to_quiz'),
    path('<slug:slug>/<int:question_id>/add_option/', add_option_view, name='add_option'),
    path('questions/<int:question_id>/', QuestionDetailsView.as_view(), name='question_details'),
    path('questions/<int:question_id>/edit_question/', EditQuestionView.as_view(), name='edit_question'),
    path('questions/<int:question_id>/', QuestionDetailsView.as_view(), name='question_details'),
    path('questions/delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
    path('questions/toggle_question/<int:pk>/', toggle_status, name='toggle_question'),

    # path('questions/<int:question_id>/delete_question/', DeleteQuestionView.as_view(), name='delete_question'),
    

]
