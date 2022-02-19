"""Question app views."""
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect,
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    ListView,
)
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalReadView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)
from quiz.models import Quiz
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
        """
        Override get method to grab quiz.
        """

        form = self.form_class
        slug = self.kwargs.get('slug')
        # question = get_object_or_404(Question, pk=pk)
        # correct_options_count = question.correct_options_count

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
        # quiz = get_object_or_404(Quiz, slug=slug)
        if form.is_valid():
            # create object manually to post user as author
            # category not included to avoid "Direct assignment 
            # of many-to-many prohibited error."
            if self.kwargs.get('slug'):
                slug = self.kwargs.get('slug')
                quiz = get_object_or_404(Quiz, slug=slug)
                category = [quiz.category]
            else:
                quiz = form.cleaned_data.get('quiz')
                # question.category.set(category)
            body = form.cleaned_data.get('body')
            featured_image = form.cleaned_data.get('featured_image')
            status = form.cleaned_data.get('status')
            question = Question.objects.create(body=body, quiz=quiz,
                                               featured_image=featured_image,
                                               author=user, status=status)
            print(form.cleaned_data)
            question.category.set(category)
            return redirect(f'../{question.pk}/details/')
        else:
            print(form.errors)

        context = {
            'form': form,
            'slug': slug,
        }
        print(slug)
        return render(self.request, 'questions/add_new_question.html', context)

   
# def add_new_question_view(request, *args, **kwargs):
#     """Add new question independently"""

#     user = request.user
#     if request.method == 'POST':
#         form = NewQuestionForm(request.POST, request.FILES)
#         if form.is_valid():
#             # create object manually to post user as author
#             # category not included to avoid "Direct assignment 
#             # of many-to-many prohibited error."
#             quiz = form.cleaned_data.get('quiz')
#             body = form.cleaned_data.get('body')
#             featured_image = form.cleaned_data.get('featured_image')
#             status = form.cleaned_data.get('status')
#             category = form.cleaned_data.get('category')
#             question = Question.objects.create(body=body, quiz=quiz,
#                                                featured_image=featured_image,
#                                                author=user, status=status)
#             print(form.cleaned_data)
#             question.category.set(category)

#             return redirect(f'../{question.pk}/details/')
#         else:
#             print(form.errors)
#     else:
#         form = NewQuestionForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'questions/add_new_question.html', context)


class CreateOptionView(BSModalCreateView):
    """Create a new option for question."""

    form_class = NewOptionForm
    template_name = 'questions/add_option_modal.html'
    success_message = 'Option created.'

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


class QuestionDetailsView(BSModalReadView):
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
            # print(slug)

        context = {
            'question': question,
            'options': options,
            'quiz': quiz,
        }
        return render(request, self.template_name, context)


class QuestionListView(ListView):
    """View listing all questions in the databae."""
    model = Question
    template_name = 'questions/manage_questions.html'

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Admin').exists():
            question_list = Question.objects.order_by('category')
            return render(request, self.template_name, {
                'question_list': question_list,
                }
            )
        else:
            return redirect('login.html')


class EditQuestionView(BSModalUpdateView):
    """Edit question elements base class."""

    model = Question
    form_class = NewQuestionForm
    template_name = 'questions/edit_question_element_modal.html'
    success_message = 'Success: Question was updated.'

    def get_success_url(self, *args, **kwargs):
        pk = self.object.pk
    
        # if self.kwargs.get('slug'):
        #     slug = self.object.quiz.slug
        #     return reverse_lazy('quiz:quiz_question_details', args=[slug, pk])
        # else:
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

    def get_success_url(self, *args, **kwargs):
        pk = self.object.question.pk
        return reverse_lazy('questions:question_details', args=[pk])


class DeleteQuestionView(BSModalDeleteView):
    """Delete question."""

    model = Question
    template_name = 'questions/question_confirm_delete.html'
    success_message = 'Question was successfully deleted.'
    # success_url = reverse_lazy('questions:manage_questions')

    def get_success_url(self, *args, **kwargs):
        """Change success url depending on whether accessed from quiz or question."""
        slug = self.kwargs.get('slug')
        print(slug)

        return reverse_lazy('questions:manage_questions')


class DeleteOptionView(BSModalDeleteView):
    """Delete option."""
    model = Option
    template_name = 'questions/option_confirm_delete.html'
    success_message = 'Success: Option was deleted.'
    # success_url = reverse_lazy('questions:question_details')

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


class SearchQuestionResultsView(ListView):
    """Search facility for questions"""

    model = Question
    context_object_name = 'questions'
    template_name = 'questions/search_question_results.html'
    queryset = Question.objects.filter(body__icontains='languages')


def upload_image(request):
    """Upload image when creating new quiz."""
    context = dict(backend_form=NewQuestionForm())

    if request.method == 'POST':
        form = NewQuestionForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'questions/add_question.html', context)


def update_image(request, pk):
    """Update image in question."""
    
    question = get_object_or_404(Question, pk=pk)
    context = {
        'backend_form': NewQuestionForm(),
        'question': question
    }
    if request.method == 'POST':
        form = NewQuestionForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'questions/edit_question_element_modal.html', context)
