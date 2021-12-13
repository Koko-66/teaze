from django.shortcuts import render
from django.views import generic
from .models import Quiz


class QuizList(generic.ListView):
    model = Quiz
    queryset = Quiz.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
