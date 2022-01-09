from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    # redirect,
    render,
    reverse
)
from django.urls import reverse_lazy
from django.views.generic import (
    # CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    # BSModalUpdateView,
    # BSModalReadView,
    BSModalDeleteView
)
from .forms import NewCategoryForm
from .models import Category
from quiz.models import Quiz
from questions.models import Question


class AddCategoryView(BSModalCreateView):
    template_name = 'categories/add_category.html'
    form_class = NewCategoryForm
    success_message = 'Success: Category was created.'
    success_url = reverse_lazy('categories:manage_categories')

    # def post(self, request):
    #     user = request.user
    #     if request.method == 'POST':
    #         form = NewCategoryForm(request.POST)
    #         if form.is_valid():
    #             name = form.cleaned_data.get('name')
    #             Category.objects.create(name=name, author=user)
    #             print(form.cleaned_data)
    #             return reverse('categories:manage_categories')
    #         else:
    #             print(form.errors)
    #     else:
    #         form = NewCategoryForm()
    
    # def get_success_url(self):
    #     return reverse('categories:manage_categories')


class EditCategoryView(UpdateView):
    template_name = 'categories/edit_category.html'
    form_class = NewCategoryForm
    queryset = Category.objects.all()

    def get_object(self):
        category_id = self.kwargs.get('id')
        return get_object_or_404(Category, id=category_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class DeleteCategoryView(BSModalDeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_message = 'Success: Category was deleted.'
    success_url = reverse_lazy('categories:manage_categories')
    
    def get_object(self):
        category_id = self.kwargs.get('id')
        return get_object_or_404(Category, id=category_id)
       
    def get(self, request, *args, **kwargs):
        category_id = self.kwargs.get('id')
        category = get_object_or_404(Category, id=category_id)
        questions = Question.objects.all()
        quizzes = Quiz.objects.all()
        protected = False
        protected_message = ''

        for question in questions:
            question_categories = question.get_categories()
            if str(category.name) in question_categories:
                protected_message = f"This category is used in question <strong>{question.body}</strong> and cannot be deleted."
                protected = True
    
        for quiz in quizzes:
            if category == quiz.category:
                protected_message = f"This category is used in quiz <strong>{quiz.title}</strong> and cannot be deleted."
                protected = True
               
        context = {
            'protected_message': protected_message,
            'protected': protected,
            'category': category,
        }
        return render(request, 'categories/category_confirm_delete.html', context)


class CategoriesListView(ListView):

    def get(self, request):
        queryset = Category.objects.all()
        return render(request, 'categories/manage_categories.html', {
            'categories': queryset
        })
