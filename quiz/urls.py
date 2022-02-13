"""Urls for quiz app"""
from django.urls import path
from quiz.views import (
    welcome_page_view,
    CreateQuizView,
    QuizListView,
    QuizDetailsView,
    EditQuizView,
    DeleteQuizView,
    AddCategoryInQuizView,
    toggle_status,
    remove_question_from_quiz,
    add_question_to_quiz,
    add_question_view,
    QuestionDetailsInQuizView,
    EditQuestionInQuizView,
    DeleteQuestionInQuizView,
    EditOptionInQuizView,
    DeleteOptionQuizView,
    CreateOptionInQuizView,
    upload_image,
    update_image,
    EditQuestionText,
    EditQuestionFeedback,
    EditQuestionQuiz,
    EditQuestionCategory,
    EditQuestionImage,
)

app_name = 'quiz'
urlpatterns = [
    path('', welcome_page_view, name='home'),
    path('quizzes/', QuizListView.as_view(), name='manage_quizzes'),
    path('quizzes/add_quiz/', CreateQuizView.as_view(), name='add_quiz'),
    path('quizzes/add_quiz/', upload_image, name='upload_image'),
    path('quizzes/<slug:slug>/details/update', update_image, name='update_image'),
    path('quizzes/<slug:slug>/details/', QuizDetailsView.as_view(), name='quiz_details'),
    path('quizzes/<slug:slug>/edit_quiz/', EditQuizView.as_view(), name='edit_quiz'),
    path('quizzes/<slug:slug>/delete_quiz/', DeleteQuizView.as_view(), name='delete_quiz'),
    path('quizzes/<slug:slug>/toggle/', toggle_status, name='toggle'),
    path('quizzes/<slug:slug>/<int:pk>/remove_question/', remove_question_from_quiz, name='remove_question'),
    path('quizzes/<slug:slug>/<int:pk>/add_question/', add_question_to_quiz, name='add_question'),
    path('quizzes/add_category', AddCategoryInQuizView.as_view(), name='add_category_in_quiz'),
    # paths for views managing questions
    path('quizzes/<slug:slug>/add_question/', add_question_view, name='add_question_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>delete_question/', DeleteQuestionInQuizView.as_view(), name='delete_question_in_quiz'),
    # paths for views for editing question elements when accessed from quiz
    path('quizzes/<slug:slug>/<int:pk>edit_question/', EditQuestionInQuizView.as_view(), name='edit_question_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/edit_question_text', EditQuestionText.as_view(), name='edit_question_text_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/edit_question_quiz', EditQuestionQuiz.as_view(), name='edit_question_quiz_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/edit_question_feedback', EditQuestionFeedback.as_view(), name='edit_question_feedback_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/edit_question_category', EditQuestionCategory.as_view(), name='edit_question_category_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/edit_question_image', EditQuestionImage.as_view(), name='edit_question_image_in_quiz'),
    # paths for viees managing options
    path('quizzes/<slug:slug>/<int:pk>/add_option/', CreateOptionInQuizView.as_view(), name='add_option_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/edit_option/', EditOptionInQuizView.as_view(), name='edit_option_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/delete_option/', DeleteOptionQuizView.as_view(), name='delete_option_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/details/', QuestionDetailsInQuizView.as_view(), name='quiz_question_details'),
    ]
