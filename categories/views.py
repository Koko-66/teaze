from django.shortcuts import get_object_or_404, reverse, render
from .forms import NewCategoryForm
from .models import Category
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)


class AddCategoryView(CreateView):
    model = Category
    form_class = NewCategoryForm
    template_name = 'categories/add_category.html'
    queryset = Category.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    


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


class DeleteCategoryView(DeleteView):
    template = 'categories/category_confirm_delete.html'

    def get_object(self):
        category_id = self.kwargs.get('id')
        return get_object_or_404(Category, id=category_id)

    def get_success_url(self):
        return reverse('quiz:home')


class CategoriesListView(ListView):
    # model = Category
    # template_name = 'categories/manage_categories.html'
    # queryset = Category.objects.all()

    def get(self, request):
        queryset = Category.objects.all()
        # template_name = 'categories/manage_categories.html'
        return render(request, 'categories/manage_categories.html', {
            'categories': queryset
        })
