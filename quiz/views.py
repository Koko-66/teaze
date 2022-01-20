# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic, View
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Quiz
from .forms import NewQuizForm
from categories.models import Category
from questions.models import Question
from results.models import Assessment


def add_quiz_view(request):
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            quiz = Quiz.objects.create(**form.cleaned_data)
            # return redirect(f'../{quiz.slug}/add_question', kwargs=[quiz.slug])
            return redirect(f'../quizzes/{quiz.slug}/details', kwargs=[quiz.slug])
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
        slug = self.kwargs.get('slug')
        return get_object_or_404(Quiz, slug=slug)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class DeleteQuizView(DeleteView):
    # queryset = Quiz.objects.all()
    template = 'quiz/delete_quiz.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Quiz, slug=slug)

    def get_success_url(self):
        return reverse('quiz:manage_quizzes')


class QuizListView(generic.ListView):
    model = Quiz
    # queryset = Quiz.objects.filter(status=1).order_by('-created_on')
    template_name = 'quiz/manage_quizzes.html'

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
        slug = self.kwargs.get('slug')
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
            'questions': questions,
            'quiz': quiz,
        }

        return render(request, 'quiz/take_quiz.html', context)


def toggle_status(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug)
    if quiz.status != 0:
        quiz.status = 0
    else:
        quiz.status = 1
    quiz.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def welcome_page_view(request):
    quiz_draft_count = Quiz.objects.filter(status=0).count()
    quiz_published_count = Quiz.objects.filter(status=1).count()
    question_draft_count = Question.objects.filter(status=0).count()
    question_published_count = Question.objects.filter(status=1).count()
    categories_count = Category.objects.all().count()

    if request.user.groups.filter(name='Admin').exists():
        quiz_list = Quiz.objects.order_by('-created_on')
    else:
        quiz_list = Quiz.objects.filter(status=1).order_by('-created_on')

    if request.user.is_authenticated:
        assessments = Assessment.objects.filter(user=request.user)
        completed_quizzes = []
        for assessment in assessments:
            completed_quizzes.append(assessment.quiz)

        # return render(request, self.template_name, {
        #     'completed_quizzes': completed_quizzes,
        #     'assessments': assessments,
        #     'quiz_list': quiz_list,
        #     }
        # )
    else:
        return redirect('account_login')

    context = {
        'quiz_draft_count': quiz_draft_count,
        'quiz_published_count': quiz_published_count,
        'question_draft_count': question_draft_count,
        'question_published_count': question_published_count,
        'categories_count': categories_count,

        'completed_quizzes': completed_quizzes,
        'assessments': assessments,
        'quiz_list': quiz_list,
    }
    return render(request, 'index.html', context)
