"""Question app views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalReadView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)
from quiz.models import Quiz
from results.models import Answer
from .filters import QuestionFilter
from .forms import (
    NewQuestionForm,
    NewOptionForm,
    EditQuestionTextForm,
    EditQuestionFeedbackForm,
    EditQuestionQuizForm,
    EditQuestionCategoryForm,
    EditQuestionImageForm
)
from .models import Question, Option


class CreateQuestionView(CreateView):
    """Add new question independently view"""
    template_name = 'questions/add_new_question.html'
    form_class = NewQuestionForm
    success_message = 'Question created successfully.'

    def get(self, *args, **kwargs):
        """Override get method to grab quiz."""
        form = self.form_class
        slug = self.kwargs.get('slug')

        context = {
            'form': form,
            'slug': slug,
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        """Override the default post method"""
        user = self.request.user
        form = self.form_class(self.request.POST, self.request.FILES)
        slug = self.kwargs.get('slug')
        if form.is_valid():
            # create object manually to post user as author
            # category added later using set() to avoid "Direct assignment
            # of many-to-many prohibited error."
            if self.kwargs.get('slug'):
                slug = self.kwargs.get('slug')
                quiz = get_object_or_404(Quiz, slug=slug)
                category = [quiz.category]
            else:
                quiz = form.cleaned_data.get('quiz')
                category = form.cleaned_data.get('category')

            body = form.cleaned_data.get('body')
            featured_image = form.cleaned_data.get('featured_image')
            feedback = form.cleaned_data.get('feedback')
            question = Question.objects.create(body=body, quiz=quiz,
                                               featured_image=featured_image,
                                               author=user, status=0,
                                               feedback=feedback)
            question.category.set(category)
            print(form.cleaned_data)
            return redirect(f'../{question.pk}/details/')
        else:
            print(form.errors)

        context = {
            'form': form,
            'slug': slug,
        }
        print(slug)
        return render(self.request, 'questions/add_new_question.html', context)


class CreateOptionView(LoginRequiredMixin, BSModalCreateView):
    """Create a new option for question."""

    form_class = NewOptionForm
    template_name = 'questions/add_option_modal.html'
    success_message = 'Option created successfully.'

    def get(self, *args, **kwargs):
        """
        Override get method to grab question and check existing
        options for 'is_correct'.
        """

        form = NewOptionForm()
        pk = self.kwargs.get('pk')
        question = get_object_or_404(Question, pk=pk)
        correct_options_count = question.correct_options_count

        context = {
            'form': form,
            'question': question,
            'correct_options_count': correct_options_count
        }

        return render(self.request, 'questions/add_option_modal.html', context)

    def post(self, *args, **kwargs):
        """Override default post method to include question info."""
        pk = self.kwargs.get('pk')
        question = get_object_or_404(Question, pk=pk)
        user = self.request.user
        form = NewOptionForm(self.request.POST)
        if form.is_valid():
            option_text = form.cleaned_data.get('option')
            is_correct = form.cleaned_data.get('is_correct')
            Option.objects.update_or_create(question=question,
                                            option=option_text,
                                            is_correct=is_correct, author=user)
            print(form.cleaned_data)
        return redirect('../details')


class QuestionDetailsView(LoginRequiredMixin, BSModalReadView):
    """Question details view."""
    model = Question
    template_name = 'questions/question_details_page.html'

    def get(self, request, *args, **kwargs):
        """Override the get method to pass in slug for redirection checks."""
        queryset = Question.objects.all()
        pk = self.kwargs.get('pk')
        question = get_object_or_404(queryset, pk=pk)
        options = question.options.all()
        quiz = None
        if self.kwargs.get('slug'):
            slug = self.kwargs.get('slug')
            quiz = get_object_or_404(Quiz, slug=slug)

        context = {
            'question': question,
            'options': options,
            'quiz': quiz,
        }
        return render(request, self.template_name, context)


class EditQuestionView(LoginRequiredMixin, BSModalUpdateView):
    """Edit question elements base class."""

    model = Question
    form_class = NewQuestionForm
    template_name = 'questions/edit_question_element_modal.html'
    success_message = 'Question updated successfully.'

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('questions:question_details', args=[pk])


# ---- Views to edit question elments ---
class EditQuestionText(EditQuestionView, BSModalUpdateView):
    """Edit the question's content."""

    form_class = EditQuestionTextForm


class EditQuestionQuiz(EditQuestionView, BSModalUpdateView):
    """Edit quiz assigned to the question."""

    form_class = EditQuestionQuizForm


class EditQuestionFeedback(EditQuestionView, BSModalUpdateView):
    """Edit question feedback."""

    form_class = EditQuestionFeedbackForm


class EditQuestionCategory(EditQuestionView, BSModalUpdateView):
    """Edit categories assigned to the question."""

    form_class = EditQuestionCategoryForm


class EditQuestionImage(EditQuestionView, BSModalUpdateView):
    """Edit image assigned to the question."""

    form_class = EditQuestionImageForm


class EditOptionView(LoginRequiredMixin, BSModalUpdateView):
    """Edit options."""

    model = Option
    template_name = 'questions/edit_option.html'
    form_class = NewOptionForm
    success_message = 'Option updated successfully.'

    def get_success_url(self, *args, **kwargs):
        pk = self.object.question.pk
        return reverse_lazy('questions:question_details', args=[pk])


class DeleteQuestionView(LoginRequiredMixin, BSModalDeleteView):
    """Delete question."""

    model = Question
    template_name = 'questions/question_confirm_delete.html'
    success_message = 'Question deleted successfully.'

    def get(self, *args, **kwargs):
        """Override the default get function."""
        pk = self.kwargs.get('pk')
        question = get_object_or_404(Question, pk=pk)
        protected = False
        protected_message = ''

        # Check if question exists in answers:
        # if yes, prevent deletion displaying message to the user,
        # if not, ask the user to confirm deletion.
        answers = Answer.objects.all()
        for answer in answers:
            if question == answer.question:
                protected_message = """This question appears in an
                assessments and cannot be deleted."""
                protected = True

        context = {
            'protected_message': protected_message,
            'protected': protected,
            'question': question,
        }
        return render(self.request, 'questions/question_confirm_delete.html',
                      context)

    def get_success_url(self, *args, **kwargs):
        """
        Change success url depending on whether
        accessed from quiz or question.
        """

        slug = self.kwargs.get('slug')
        print(slug)
        return reverse_lazy('questions:manage_questions')


class DeleteOptionView(LoginRequiredMixin, BSModalDeleteView):
    """Delete option."""
    model = Option
    template_name = 'questions/option_confirm_delete.html'
    success_message = 'Option deleted successfully.'

    def get(self, *args, **kwargs):
        """Override the default get function."""
        pk = self.kwargs.get('pk')
        option = get_object_or_404(Option, pk=pk)
        answers = Answer.objects.all()
        protected = False
        protected_message = ''

        # Check if question exists in answers:
        # if yes, prevent deletion displaying message to the user,
        # if not, ask the user to confirm deletion.
        for answer in answers:
            if answer.answer == option:
                protected_message = """This option appears in an
                assessments and cannot be deleted."""
                protected = True

        context = {
            'protected_message': protected_message,
            'protected': protected,
            'option': option,
        }
        return render(self.request, 'questions/option_confirm_delete.html',
                      context)

    def get_success_url(self, *args, **kwargs):
        pk = self.object.question.pk
        return reverse_lazy('questions:question_details', args=[pk])


def toggle_question_status(request, pk, *args, **kwargs):
    """Toggle question status between Draft (0) and Approved (1)."""
    question = get_object_or_404(Question, pk=pk)
    if question.status != 0:
        question.status = 0
    else:
        question.status = 1
    question.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Code for checkting if filter is filled from:
# https://stackoverflow.com/questions/49732359/check-and-clear-filters-with-django-filter
def search(request):
    """Filter qustions"""
    question_list = Question.objects.all()
    question_filter = QuestionFilter(request.GET, queryset=question_list)
    has_filter = any(field in request.GET for field in
                     set(question_filter.get_fields()))
    print(has_filter)

    template = 'questions/manage_questions.html'
    context = {
        'filter': question_filter,
        'has_filter': has_filter,
        }
    return render(request, template, context)
