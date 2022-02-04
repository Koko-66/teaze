"""Question app views."""
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect,
    # render_to_response
)
from django.urls import reverse_lazy
from django.views.generic import (
    # CreateView,
    ListView,
    # UpdateView
)
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalReadView,
    # BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)
# from .forms import NewOptionForm, NewQuestionForm, EditQuestionTextForm
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
# from quiz.models import Quiz


def add_new_question_view(request, *args, **kwargs):
    """Add new question independently"""

    user = request.user
    if request.method == 'POST':
        form = NewQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            # create object manually to post user as author
            quiz = form.cleaned_data.get('quiz')
            body = form.cleaned_data.get('body')
            featured_image = form.cleaned_data.get('featured_image')
            status = form.cleaned_data.get('status')
            category = form.cleaned_data.get('category')
            question = Question.objects.create(body=body, quiz=quiz,
                                               featured_image=featured_image,
                                               category=category,
                                               author=user, status=status)
            print(form.cleaned_data)
            return redirect(f'../{question.id}/add_new_option',
                            args=[question.pk])
        else:
            print(form.errors)
    else:
        form = NewQuestionForm()

    context = {
        'form': form,
        # 'quiz': quiz,
    }
    return render(request, 'questions/add_new_question.html', context)


def add_new_option_view(request, pk):
    """Add new option independently"""
    user = request.user
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = NewOptionForm(request.POST)
        if form.is_valid():
            option = form.cleaned_data.get('option')
            # position = form.cleaned_data.get('position')
            is_correct = form.cleaned_data.get('is_correct')
            option = Option.objects.create(question=question, option=option,
                                           is_correct=is_correct, author=user)
            print(form.cleaned_data)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)
    else:
        form = NewOptionForm()

    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'questions/add_option.html', context)


class QuestionDetailsView(BSModalReadView):
    """Question details view."""
    model = Question
    # template_name = 'questions/question_details_page.html'

    def get(self, request, pk, *args, **kwargs):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        options = question.options.all()

        return render(
            request,
            "questions/question_details_page.html",
            {
                "question": question,
                "options": options,
            },
        )


class QuestionListView(ListView):
    """View listing all questions in the databae."""
    model = Question
    template_name = 'questions/manage_questions.html'

    def get(self, request):
        if request.user.groups.filter(name='Admin').exists():
            question_list = Question.objects.order_by('category')
            return render(request, self.template_name, {
                'question_list': question_list,
                }
            )
        else:
            return redirect('login.html')


# class EditQuestionView(BSModalUpdateView):
#     """Edit question."""

#     model = Question
#     template_name = 'questions/edit_question.html'
#     form_class = NewQuestionForm
#     success_message = 'Success: Question was updated.'
#     success_url = reverse_lazy('questions:question_details')


class EditQuestionView(BSModalUpdateView):
    """Edit question elements base class."""

    model = Question
    form_class = NewQuestionForm
    template_name = 'questions/edit_question_element_modal.html'
    success_message = 'Success: Question was updated.'

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


class EditOptionView(BSModalUpdateView):
    """Edit options."""

    model = Option
    template_name = 'questions/edit_option.html'
    form_class = NewOptionForm

    def get_success_url(self):
        slug = self.object.question.quiz.slug
        pk = self.object.question.pk

        return reverse_lazy('quiz:add_option_in_quiz', args=[slug, pk])


class DeleteQuestionView(BSModalDeleteView):
    """Delete question."""

    model = Question
    template_name = 'questions/question_confirm_delete.html'
    success_message = 'Success: Category was deleted.'
    success_url = reverse_lazy('questions:manage_questions')


class DeleteOptionView(BSModalDeleteView):
    """Delete option."""
    model = Option
    template_name = 'questions/option_confirm_delete.html'
    success_message = 'Success: Option was deleted.'
    # success_url = reverse_lazy('questions:question_details')

    def get_success_url(self):
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


# def toggle_is_correct(request, pk, *args, **kwargs):
#     option = get_object_or_404(Option, pk=pk)
#     if option.is_correct is not False:
#         option.is_correct = True
#     else:
#         option.is_correct = True
#     option.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
