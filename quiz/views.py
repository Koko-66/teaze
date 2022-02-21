# from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect
    )
from django.views import generic
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    # BSModalReadView,
    BSModalUpdateView,
)
from categories.models import Category
from categories.forms import NewCategoryForm
from questions.forms import (
    # NewOptionForm,
    EditQuestionTextForm,
    EditQuestionFeedbackForm,
    EditQuestionQuizForm,
    EditQuestionCategoryForm,
    EditQuestionImageForm,)
from questions.models import Question
from questions.views import (
    CreateOptionView,
    CreateQuestionView,
    DeleteOptionView,
    DeleteQuestionView,
    EditOptionView,
    EditQuestionView,
    QuestionDetailsView,
    )
from results.models import Assessment
from .models import Quiz
from .forms import (
    NewQuizForm,
    AddQuestionToQuizForm,
    # ToggleQuizStatusForm,
)


# class Error(Exception):
#     """Base class for other exceptions"""
#     pass

# class CorrectAlreadyExists(Error):
#     """Raised when the input value is too small"""
#     pass


def welcome_page_view(request):
    """Landing page - view for the index.html"""

    quiz_draft_count = Quiz.objects.filter(status=0).count()
    quiz_published_count = Quiz.objects.filter(status=1).count()
    question_draft_count = Question.objects.filter(status=0).count()
    question_published_count = Question.objects.filter(status=1).count()
    categories_count = Category.objects.all().count()
    assessment = None
    completed_quizzes = []
    
    if request.user.groups.filter(name='Admin').exists():
        quiz_list = Quiz.objects.order_by('-created_on')
    else:
        quiz_list = Quiz.objects.filter(status=1).order_by('-created_on')

    if request.user.is_authenticated:
        assessments = Assessment.objects.filter(user=request.user)    
        for assessment in assessments:
            completed_quizzes.append(assessment.quiz)
            assessment = assessment
    else:
        return redirect('account_login')

    context = {
        'quiz_draft_count': quiz_draft_count,
        'quiz_published_count': quiz_published_count,
        'question_draft_count': question_draft_count,
        'question_published_count': question_published_count,
        'categories_count': categories_count,

        'completed_quizzes': completed_quizzes,
        # 'assessments': assessments,
        'quiz_list': quiz_list,
        'assessment': assessment
    }
    return render(request, 'index.html', context)


# Add, Edit and display quizzes views
class CreateQuizView(generic.CreateView):
    """Create new quiz."""

    template_name = 'quiz/add_quiz.html'
    form_class = NewQuizForm
    success_message = 'Quiz created successfully.'

    def get_success_url(self):
        slug = self.object.slug
        return reverse_lazy('quiz:quiz_details', args=[slug])


class EditQuizView(generic.UpdateView):
    """Edit quiz"""
    template_name = 'quiz/edit_quiz.html'
    form_class = NewQuizForm
    queryset = Quiz.objects.all()


class DeleteQuizView(generic.DeleteView):
    """Delete quiz"""
    queryset = Quiz.objects.all()
    template = 'quiz/delete_quiz.html'
    success_url = reverse_lazy('quiz:manage_quizzes')


class QuizListView(generic.ListView):
    """Display list of quizzes depending on type of user."""
    model = Quiz
    template_name = 'quiz/manage_quizzes.html'

    def get(self, request, *args, **kwargs):
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


class QuizDetailsView(generic.DetailView):
    """Quiz details view."""

    template_name = 'quiz/quiz_detail.html'

    def get(self, *args, **kwargs):
        """Overwrite the default get function to render available qustions
        with the same category."""
        
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

        return render(self.request, self.template_name, context)


# class ToggleQuizStatusView(BSModalUpdateView):
#     """Toggle quiz status"""
#     model = Quiz
#     template_name = 'quiz/confirm_change_status.html'
#     form_class = ToggleQuizStatusForm
#     success_message = "Status changed"
    
#     def get(self, *args, **kwargs):
#         slug = self.kwargs.get('slug')
#         quiz = get_object_or_404(Quiz, slug=slug)
#         form = self.form_class
#         if quiz.status == 0:
#             message = "will change to approve"
            
#         if quiz.status == 1:
#             message = "will change to approve"
#         quiz.toggle_status()
#         context = {
#             'quiz': quiz,
#             'message': message,
#             'form': form,
#         }
#         return render(self.request, self.template_name, context)

    # def get_success_url(self, *args, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     return reverse_lazy('quiz:quiz_details', args=[slug])

def toggle_status(request, slug, *args, **kwargs):
    """"Togge quiz status."""
    quiz = get_object_or_404(Quiz, slug=slug)
    if quiz.status == 0:
        messages.warning(request, 'Quiz has been set as Approved. It is now accessible to test takers.')
    else:
        messages.success(request, 'Quiz status changed to Draft.')
    quiz.toggle_status()
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


class CreateQuestionInQuizView(CreateQuestionView):
    """
    Add new question from quiz details view. Inherits from 
    CreateQuestionView in questions app and changes the form.
    """
    form_class = AddQuestionToQuizForm


# Managing options while accessed from quiz view
class CreateOptionInQuizView(CreateOptionView):
    """Create a new option for question."""


class EditOptionInQuizView(EditOptionView):
    """Edit option while in quiz."""

    def get_success_url(self, *args, **kwargs):
        """Override success url from base class."""
        pk = self.object.question.pk
        slug = self.kwargs.get('slug')
        return reverse_lazy('quiz:quiz_question_details', args=[slug, pk])

class DeleteOptionQuizView(DeleteOptionView):
    """Delete option."""

    def get_success_url(self, *args, **kwargs):
        pk = self.object.question.pk
        slug = self.kwargs.get('slug')
        return reverse_lazy('quiz:quiz_question_details', args=[slug, pk])


class EditQuestionInQuizView(EditQuestionView):
    """Edit question when in detail view accessed from quiz."""

    def get_success_url(self, *args, **kwargs):
        """Override success url from base class."""
        slug = self.kwargs.get('slug')
        pk = self.kwargs.get('pk')
        return reverse_lazy('quiz:quiz_question_details', args=[slug, pk])

    # ---- Views to edit question elments ---
class EditQuestionText(EditQuestionInQuizView, BSModalUpdateView):
    """Edit the question's content."""

    form_class = EditQuestionTextForm


class EditQuestionQuiz(EditQuestionInQuizView, BSModalUpdateView):
    """Edit quiz assigned to the question."""

    form_class = EditQuestionQuizForm


class EditQuestionFeedback(EditQuestionInQuizView, BSModalUpdateView):
    """Edit question feedback."""

    form_class = EditQuestionFeedbackForm


class EditQuestionCategory(EditQuestionInQuizView, BSModalUpdateView):
    """Edit categories assigned to the question."""

    form_class = EditQuestionCategoryForm


class EditQuestionImage(EditQuestionInQuizView, BSModalUpdateView):
    """Edit image assigned to the question."""

    form_class = EditQuestionImageForm


class DeleteQuestionInQuizView(DeleteQuestionView):
    """Delete question."""

    def get_success_url(self, *args, **kwargs):
        """Override success url from base class."""
        slug = self.kwargs.get('slug')
        return reverse_lazy('quiz:quiz_details', args=[slug])


class QuestionDetailsInQuizView(QuestionDetailsView):
    """View question details in quiz details view.
    Inherits from QuestionDetailView in question app with different path."""

