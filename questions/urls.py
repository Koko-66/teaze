"""Urls for questions app"""
from django.urls import path
from .views import (
    add_question_view,
    # AddOptionView,
    add_option_view,
    QuestionDetailsView,
    EditQuestionView,
    # DeleteQuestionView,
    question_delete_view,
    QuestionListView,
)

app_name = 'questions'

urlpatterns = [
    # path('questions/add_question/', AddQuestionView.as_view(), name='add_question') 
    path('<slug:slug>/add_question/', add_question_view, name='add_question'),
    path('<slug:slug>/<int:question_id>/add_option/', add_option_view, name='add_option'),
    path('questions/manage_questions/', QuestionListView.as_view(), name='manage_questions'),
    path('questions/<int:question_id>/', QuestionDetailsView.as_view(), name='question_details'),
    path('questions/<int:question_id>/edit_question/', EditQuestionView.as_view(), name='edit_question'),
    path('questions/<int:question_id>/delete_question/', question_delete_view, name='delete_question'),
    # path('questions/<int:question_id>/delete_question/', DeleteQuestionView.as_view(), name='delete_question'),
    

]
