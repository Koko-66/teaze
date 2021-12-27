# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Quiz
from .forms import NewQuizForm
from results.models import Assessment


def add_quiz_view(request):
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            quiz = Quiz.objects.create(**form.cleaned_data)
            return redirect(f'../{quiz.slug}/add_question', kwargs=[quiz.slug])
        else:
            print(form.errors)
    else:
        form = NewQuizForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/add_quiz.html', context)


# class AddQuizView(CreateView):
#     model = Quiz
#     form_class = NewQuizForm
#     template_name = 'quiz/add_quiz.html'
#     queryset = Quiz.objects.all()

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)


class EditQuizView(UpdateView):
    template_name = 'quiz/edit_quiz.html'
    form_class = NewQuizForm
    queryset = Quiz.objects.all()

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Quiz, slug=slug)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class DeleteQuizView(DeleteView):
    # queryset = Quiz.objects.all()
    template = 'quiz/delete_quiz.html'

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Quiz, slug=slug)

    def get_success_url(self):
        return reverse('quiz:home')


class QuizListView(generic.ListView):
    model = Quiz
    # queryset = Quiz.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get(self, request):
        if request.user.groups.filter(name='Admin').exists():
            quiz_list = Quiz.objects.order_by('-created_on')
        else:
            quiz_list = Quiz.objects.filter(status=1).order_by('-created_on')

        if request.user.is_authenticated:
            assessments = Assessment.objects.filter(user=request.user)
            completed_quizzes = []
            for assessment in assessments:
                completed_quizzes.append(assessment.quiz)

            return render(request, self.template_name, {
                'completed_quizzes': completed_quizzes,
                'assessments': assessments,
                'quiz_list': quiz_list,
                }
            )
        else:
            return redirect('account_login')


class QuizDetailsView(DetailView):
    # queryset = Quiz.objects.all()
    template = 'quiz/quiz_detail.html'

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Quiz, slug=slug)


class TakeQuizView(View):

    def get(self, request, slug):
        queryset = Quiz.objects.filter(status=1)
        quiz = get_object_or_404(queryset, slug=slug)
        questions = []
        for question in quiz.get_questions():
            options = []
            for option in question.get_options():
                options.append(option)
            questions.append({question: options})

        context = {
            "questions": questions,
            "quiz": quiz,
        }

        return render(request, "quiz/take_quiz.html", context)
