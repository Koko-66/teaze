from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    reverse
)
from .forms import NewCategoryForm
from .models import Category
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)


# class AddCategoryView(CreateView):
#     model = Category
#     form_class = NewCategoryForm
#     template_name = 'categories/add_category.html'
#     queryset = Category.objects.all()

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
    
def add_category_view(request):
    user = request.user
    if request.method == 'POST':
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            Category.objects.create(name=name, author=user)
            print(form.cleaned_data)
            return redirect('../')
        else:
            print(form.errors)
    else:
        form = NewCategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'categories/add_category.html' , context)


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
        return reverse('categories:manage_categories')


class CategoriesListView(ListView):

    def get(self, request):
        queryset = Category.objects.all()
        return render(request, 'categories/manage_categories.html', {
            'categories': queryset
        })
