from . import views
from django.urls import path


urlpatterns = [
    path('', views.QuizList.as_view(), name='home')
    ]

