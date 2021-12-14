from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Quiz


class QuizList(generic.ListView):
    model = Quiz
    queryset = Quiz.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class QuizDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Quiz.objects.filter(status=1)
        quiz = get_object_or_404(queryset, slug=slug)
        title = quiz.title
        # Code below adapted from tutorial prepared by Pyplane (youtube.com/watch?v=T9xOjVJI1rg)
        questions = []
        for question in quiz.get_questions():
            options = []
            for option in question.get_options():
                options.append({option.pk: option.option})
            questions.append({question.pk: {question.body: options}})

        return render(
            request,
            "quiz_detail.html",
            {
                "title": title,
                "questions": questions,

            },
        )
