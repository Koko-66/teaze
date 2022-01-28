"""Urls for questions app"""
from django.urls import path
from .views import (
    # AddQuestionView,
    add_new_question_view,
    add_question_view,
    # AddOptionView,
    add_option_view,
    add_new_option_view,
    QuestionDetailsView,
    EditQuestionView, 
    DeleteQuestionView,
    QuestionListView,
    toggle_question_status,
    EditOptionView,
    toggle_is_correct,
    DeleteOptionView,
)

app_name = 'questions'

urlpatterns = [
    # urls for questions from question management views
    path('questions/', QuestionListView.as_view(), name='manage_questions'),
    path('questions/<int:pk>/', QuestionDetailsView.as_view(), name='question_details'),
    # path('questions/add_new_question/', AddQuestionView.as_view(), name='add_new_question'),
    path('questions/add_new_question/', add_new_question_view, name='add_new_question'),
    path('questions/edit_question/<int:pk>/', EditQuestionView.as_view(), name='edit_question'),
    path('questions/delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
    path('questions/<int:pk>/toggle/', toggle_question_status, name='toggle_question'),
    # urls for questions from question management views
    path('quizzes/<slug:slug>/add_question/', add_question_view, name='add_question_in_quiz'),
    # urls for options
    path('quizzes/<slug:slug>/<int:pk>/add_option/', add_option_view, name='add_option_in_quiz'),
    path('questions/<int:pk>/add_new_option/', add_new_option_view, name='add_new_option'),
    path('questions/edit_question/<int:pk>/edit_option/', EditOptionView.as_view(), name='edit_option'),
    path('questions/edit_question/<int:pk>/option/toggle_is_correct', toggle_is_correct, name='toggle_is_correct'),
    path('questions/delete_option/<int:pk>/', DeleteOptionView.as_view(), name='delete_option')
]

