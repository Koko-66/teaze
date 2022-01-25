from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect
)
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalReadView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)
from .forms import NewOptionForm, NewQuestionForm, AddQuestionToQuizForm
from .models import Question, Option
from quiz.models import Quiz

    
def add_new_question_view(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            # create object manually to post user as author
            quiz = form.cleaned_data.get('quiz')
            body = form.cleaned_data.get('body')
            featured_image = form.cleaned_data.get('featured_image')
            status = form.cleaned_data.get('status')
            category = form.cleaned_data.get('category')
            question = Question.objects.create(body=body, quiz=quiz,
                                                featured_image=featured_image,
                                                author=user, status=status)
            print(form.cleaned_data)
            return redirect(f'../{question.id}/add_new_option', args=[question.id])
        else:
            print(form.errors)
    else:
        form = NewQuestionForm()

    context = {
        'form': form,
        # 'quiz': quiz,
    }
    return render(request, 'questions/add_new_question.html', context)


def add_question_view(request, slug):
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


# HANDLE INTEGRITY ERROR if keeping position!
def add_new_option_view(request, pk):
    user = request.user
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = NewOptionForm(request.POST)
        if form.is_valid():
            option = form.cleaned_data.get('option')
            position = form.cleaned_data.get('position')
            is_correct = form.cleaned_data.get('is_correct')
            option = Option.objects.create(question=question, option=option,
                                           position=position,
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

 
# HANDLE INTEGRITY ERROR if keeping position!
def add_option_view(request, slug, pk):
    user = request.user
    quiz = get_object_or_404(Quiz, slug=slug)
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = NewOptionForm(request.POST)
        if form.is_valid():
            option = form.cleaned_data.get('option')
            position = form.cleaned_data.get('position')
            is_correct = form.cleaned_data.get('is_correct')
            option = Option.objects.create(question=question, option=option,
                                           position=position,
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

    model = Question
    template_name = 'questions/question_details.html'

    def get(self, request, pk, *args, **kwargs):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        options = question.options.all()

        return render(
            request,
            "questions/question_details.html",
            {
                "question": question,
                "options": options,
            },
        )

class QuestionListView(ListView):
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


class EditQuestionView(BSModalUpdateView):
    """Edit question."""

    model = Question
    template_name = 'questions/edit_question.html'
    form_class = NewQuestionForm
    success_message = 'Success: Question was updated.'
    success_url = reverse_lazy('questions:manage_questions')


class DeleteQuestionView(BSModalDeleteView):
    """Delete question."""

    model = Question
    template_name = 'questions/question_confirm_delete.html'
    success_message = 'Success: Category was deleted.'
    success_url = reverse_lazy('questions:manage_questions')


def toggle_question_status(request, pk, *args, **kwargs):
    question = get_object_or_404(Question, pk=pk)
    if question.status != 0:
        question.status = 0
    else:
        question.status = 1
    question.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
