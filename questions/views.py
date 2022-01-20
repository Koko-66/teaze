from django.http import JsonResponse
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    # reverse
)
from django.urls import reverse_lazy
from django.views.generic import (
    # DetailView,
    # UpdateView,
    # DeleteView,
    ListView,
    # View
)
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


class AddQuestionView(BSModalCreateView):
    """Add new question independently, from question management view."""

    template_name = 'questions/add_question-modal.html'
    form_class = NewQuestionForm
    success_message = 'Success: Question was created.'
    success_url = reverse_lazy('questions:add_question')


class AddOptionView(BSModalCreateView):
    template_name = 'questions/add_option.html'
    form_class = NewOptionForm
    success_message = 'Success: Option was created.'
    success_url = reverse_lazy('questions:add_question')


def add_question_view(request, slug):
    user = request.user
    quiz = get_object_or_404(Quiz, slug=slug)
    quiz_title = quiz.title
    if request.method == 'POST':
        form = AddQuestionToQuizForm(request.POST)
        if form.is_valid():
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


def add_option_view(request, slug, question_id):
    user = request.user
    quiz = get_object_or_404(Quiz, slug=slug)
    question = get_object_or_404(Question, id=question_id)
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
            return redirect('../add_option',
                            args=[question.id, quiz.slug])
        else:
            print(form.errors)
    else:
        form = NewOptionForm()

    context = {
        'form': form,
        'question': question,
        'quiz': quiz,
        # 'question_id': question.id,
        # 'quiz_slug': quiz.slug,
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


def toggle_question_status(request):
   
    print(request.POST)
    if request.method == "POST":
        status_value = request.POST['status']
        question_id = request.POST['id']
        question = get_object_or_404(Question, pk=question_id)
        question.status = status_value
        print(status_value, question_id)
        print(f"Question status: {question.status}")
        question.save()

    return render(request, 'questions/question_details.html', {
        'question': question,
    })
    # return JsonResponse({'text': 'works'})
    # question = get_object_or_404(Question, pk=pk)
    # if question.status != 0:
    #     question.status = 0
    # else:
    #     question.status = 1
    # question.save()
    # return redirect(manage_questions)

# class QuestionDetailsView(DetailView):
#     model = Question
#     template_name = 'questions/question_details.html'
#     queryset = Question.objects.all()

#     def get_object(self):
#         question_id = self.kwargs.get("id")
#         return get_object_or_404(Question, id=question_id)


# class EditQuestionView(View):
#     model = Question
#     template_name = 'questions/edit_question.html'
#     form_class = NewQuestionForm
    
#     def get_object(self):
#         queryset = Question.objects.all()
#         question_id = self.kwargs.get('id')
#         return get_object_or_404(queryset, id=question_id)

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)



# class AddQuestionView(CreateView):

#     model = Question
#     form_class = NewQuestionForm()
#     template_name = 'questions/add_question.html'
#     success_url = '/'
    

# class AddOptionView(CreateView):

#     model = Option
#     form_class = NewOptionForm
#     template_name = 'questions/add_option.html'
#     # success_url = '/'

    # context = {
    #     'form': form,
    # }
    # return render(request, 'quiz/add_quiz.html', context)
