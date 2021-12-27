from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse
)
from django.views.generic import (
    # DetailView,
    UpdateView,
    DeleteView,
    ListView,
    View
)
from .forms import NewOptionForm, NewQuestionForm
from .models import Question, Option
from quiz.models import Quiz


def add_question_view(request, slug):
    user = request.user
    quiz = get_object_or_404(Quiz, slug=slug)
    quiz_title = quiz.title
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
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
        form = NewQuestionForm()

    context = {
        'form': form,
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
            return redirect(f'../add_option',
                            args=[question.id, quiz.slug])
        else:
            print(form.errors)
    else:
        form = NewOptionForm()

    context = {
        'form': form,
        'question_id': question.id,
        'quiz_slug': quiz.slug,
    }
    return render(request, 'questions/add_option.html', context)


class QuestionDetailsView(View):

    def get(self, request, question_id, *args, **kwargs):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, id=question_id)
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


class EditQuestionView(View):

    def get(self, request, question_id, *args, **kwargs):
        question = get_object_or_404(Question, id=question_id)
        if request.method == 'POST':
            form = NewQuestionForm(request.POST, instance=question)
            fields = __all__
            if form.is_valid():
                form.save()
                return redirect('questions/manage_questions')

        form = NewQuestionForm(instance=question)
        context = {
                "form": form,
            }
        return render(request, "questions/edit_question.html", context)


def question_delete_view(request, question_id, *args, **kwargs):
    obj = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'object': obj
    }
    return render(request, 'questions/question_confirm_delete.html', context)



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


# class DeleteQuestionView(DeleteView):
#     template = 'questions/question_confirm_delete.html'
#     queryset = Question.objects.all()

#     def get_object(self):
#         question_id = self.kwargs.get('id')
#         return get_object_or_404(Question, id=question_id)

#     def get_success_url(self):
#         return reverse('quiz:home')


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
