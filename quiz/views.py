from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, DetailView
from .models import Quiz
from .forms import NewQuizForm
from results.models import Assessment


class AddQuizView(CreateView):
    model = Quiz
    form_class = NewQuizForm
    template_name = 'quiz/add_quiz.html'
    # form.instance.name = request.user.username
    queryset = Quiz.objects.all()
    # success_url = 'new_question'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return 'new_question'

# class DeleteQuiz()

# def add_quiz_view(request):
#     form = NewQuizForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = NewQuizForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'quiz/add_quiz.html', context)


class QuizListView(generic.ListView):
    model = Quiz
    # queryset = Quiz.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get(self, request):
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
            return redirect('account_signup')


class QuizDetailsView(DetailView):
    queryset = Quiz.objects.all()
    template = 'quiz/quiz_detail.html'


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
