"""Urls for questions app"""
from django.urls import path
# from .views import *
from .views import (
    add_new_question_view,
    add_new_option_view,
    QuestionDetailsView,
    EditQuestionView, 
    EditQuestionText,
    DeleteQuestionView,
    QuestionListView,
    toggle_question_status,
    EditOptionView,
    # toggle_is_correct,
    DeleteOptionView,
)

app_name = 'questions'

urlpatterns = [
    # urls for questions from question management views
    path('questions/', QuestionListView.as_view(), name='manage_questions'),
    path('questions/<int:pk>/', QuestionDetailsView.as_view(), name='question_details'),
    # path('questions/add_new_question/', AddQuestionView.as_view(), name='add_new_question'),
    path('questions/add_new_question/', add_new_question_view, name='add_new_question'),
    path('questions/<int:pk>/edit_question/', EditQuestionView.as_view(), name='edit_question'),
    path('questions/delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
    path('questions/<int:pk>/toggle/', toggle_question_status, name='toggle_question'),
    path('questions/<int:pk>/add_new_option/', add_new_option_view, name='add_new_option'),
    path('questions/<int:pk>/edit_option/', EditOptionView.as_view(), name='edit_option'),
    # path('questions/<int:pk>/option/toggle_is_correct', toggle_is_correct, name='toggle_is_correct'),
    path('questions/<int:pk>/delete_option/', DeleteOptionView.as_view(), name='delete_option'),
    path('questions/<int:pk>/edit_question_text', EditQuestionText.as_view(), name='edit_question_text'),
    path('questions/<int:pk>/edit_question_quiz', EditQuestionQuiz.as_view(), name='edit_question_quiz'),
    path('questions/<int:pk>/edit_question_feedback', EditQuestionFeedback.as_view(), name='edit_question_feedback'),
    path('questions/<int:pk>/edit_question_category', EditQuestionCategory.as_view(), name='edit_question_category'),
    # path('questions/<int:pk>/edit_question_status', EditQuestionStatus.as_view(), name='edit_question_status'),
    path('questions/<int:pk>/edit_question_image', EditQuestionImage.as_view(), name='edit_question_image'),
]

