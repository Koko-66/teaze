"""Urls for questions app"""
from django.urls import path
from .views import (
    AddQuestionView,
    add_question_view,
    AddOptionView,
    add_option_view,
    QuestionDetailsView,
    EditQuestionView,
    DeleteQuestionView,
    QuestionListView,
    toggle_question_status,
)

app_name = 'questions'

urlpatterns = [
    # urls for questions from question management views
    path('questions/', QuestionListView.as_view(), name='manage_questions'),
    path('questions/<int:pk>/', QuestionDetailsView.as_view(), name='question_details'),
    path('questions/add_new_question/', AddQuestionView.as_view(), name='add_new_question'),
    path('questions/edit_question/<int:pk>/', EditQuestionView.as_view(), name='edit_question'),
    path('questions/delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
    path('questions/<int:pk>/toggle/', toggle_question_status, name='toggle_question'),
    # urls for questions from question management views
    path('quizzes/<slug:slug>/add_question_in_quiz/', add_question_view, name='add_question_in_quiz'),
    # urls for options
    path('quizzes/<slug:slug>/<int:question_id>/add_option/', add_option_view, name='add_option_in_quiz'),
    path('questions/<int:pk>/add_option', AddOptionView, name='add_option'),
]
