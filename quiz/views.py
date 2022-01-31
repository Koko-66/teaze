# from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect
    )
from django.views import generic, View
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalReadView,
)
from .models import Quiz
from .forms import NewQuizForm, AddQuestionToQuizForm
from categories.models import Category
from categories.forms import NewCategoryForm
from questions.forms import NewOptionForm
from questions.models import Question, Option
from results.models import Assessment


def welcome_page_view(request):
    """Landing page - view for the index.html"""

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


# Add, Edit and display quizzes views
def add_quiz_view(request):
    """Add new quiz"""

    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            quiz = Quiz.objects.create(**form.cleaned_data)
            return redirect(f'../quizzes/{quiz.slug}/details',
                            kwargs=[quiz.slug])
        else:
            print(form.errors)
    else:
        form = NewQuizForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/add_quiz.html', context)


class EditQuizView(UpdateView):
    """Edit quiz"""

    template_name = 'quiz/edit_quiz.html'
    form_class = NewQuizForm
    queryset = Quiz.objects.all()



class DeleteQuizView(DeleteView):
    """Delete quiz"""
    queryset = Quiz.objects.all()
    template = 'quiz/delete_quiz.html'
    success_url = reverse_lazy('quiz:manage_quizzes')


class QuizListView(generic.ListView):
    model = Quiz
    template_name = 'quiz/manage_quizzes.html'

    def get(self, request):
        """Overwrite get method"""
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
    queryset = Quiz.objects.all()
    template = 'quiz/quiz_detail.html'

    # def get_object(self):
    #     slug = self.kwargs.get('slug')
    #     return get_object_or_404(Quiz, slug=slug)

    def get(self, request, *args, **kwargs):
        """Overwrite the default get function to render available qustions
        with the same category."""
        template_name = 'quiz/quiz_detail.html'
        slug = self.kwargs.get('slug')
        quiz = get_object_or_404(Quiz, slug=slug)

        quiz_category = quiz.category
        questions = Question.objects.all()

        available_questions = []
        for question in questions:
            question_categories = question.get_categories()
            if str(quiz_category) in question_categories and question.quiz != quiz:
                available_questions.append(question)
        context = {
            'quiz': quiz,
            'available_questions': available_questions,
            'slug': slug,
        }

        return render(request, template_name, context)


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


def toggle_status(request, slug, *args, **kwargs):
    quiz = get_object_or_404(Quiz, slug=slug)
    if quiz.status != 0:
        quiz.status = 0
    else:
        quiz.status = 1
    quiz.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_question_from_quiz(request, pk, *args, **kwargs):
    """Remove question from the selected quiz. """

    question = get_object_or_404(Question, pk=pk)
    print(question.quiz)
    question.quiz = None
    question.save()
    print(question.quiz)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_question_to_quiz(request, pk, slug, *args, **kwargs):
    """Add question to the selected quiz."""

    quiz = get_object_or_404(Quiz, slug=slug)
    question = get_object_or_404(Question, pk=pk)
    print(quiz.slug)
    # print(question.quiz)
    question.quiz = quiz
    question.save()
    # print(question.quiz)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddCategoryInQuizView(BSModalCreateView):
    """Add new category within add new quiz view."""

    template_name = 'categories/add_category.html'
    form_class = NewCategoryForm
    success_message = 'Success: Category was created.'
    success_url = reverse_lazy('quiz:add_quiz')


def add_question_view(request, slug):
    """Add new question from quiz details view."""

    user = request.user
    quiz = get_object_or_404(Quiz, slug=slug)
    quiz_title = quiz.title
    if request.method == 'POST':
        form = AddQuestionToQuizForm(request.POST)
        if form.is_valid():
            # create object manually to post user as author
            body = form.cleaned_data.get('body')
            featured_image = form.cleaned_data.get('featured_image')
            status = form.cleaned_data.get('status')
            question = Question.objects.create(body=body, quiz=quiz,
                                               featured_image=featured_image,
                                               author=user, status=status)
            print(form.cleaned_data)
            question.category.set([quiz.category])
            return redirect(f'../{question.id}/add_option', args=[question.id])
        else:
            print(form.errors)
    else:
        form = AddQuestionToQuizForm()

    context = {
        'form': form,
        'quiz': quiz,
    }
    return render(request, 'questions/add_question.html', context)


def add_option_view(request, slug, pk):
    """"Add option to the question while in quiz."""   
    user = request.user
    quiz = get_object_or_404(Quiz, slug=slug)
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = NewOptionForm(request.POST)
        if form.is_valid():
            option = form.cleaned_data.get('option')
            # position = form.cleaned_data.get('position')
            is_correct = form.cleaned_data.get('is_correct')
            option = Option.objects.create(question=question, option=option,
                                        #    position=position,
                                           is_correct=is_correct, author=user)
            print(form.cleaned_data)
            # return redirect('../add_option', args=[question.id, quiz.slug])
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)
    else:
        form = NewOptionForm()

    context = {
        'form': form,
        'question': question,
        'quiz': quiz,
    }
    return render(request, 'questions/add_option.html', context)


class QuestionDetailsView(BSModalReadView):
    """View question details in quiz details view."""
    model = Question

    def get(self, request, slug, pk, *args, **kwargs):
        quiz = get_object_or_404(Quiz, slug=slug)
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        options = question.options.all()

        return render(
            request,
            "questions/question_details.html",
            {
                "question": question,
                "options": options,
                'quiz': quiz
            },
        )