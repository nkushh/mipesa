from django.shortcuts import render, redirect, get_object_or_404

from .models import ExpenseCategory

# Create your views here.
def categories(request):
	template = 'income/categories.html'
	context = {
		'categories' : Category.objects.all().order_by('category_name'),
	}
	return render(request, template, context)

def new_category(request):
	if request.method=="POST":
		category = request.POST['category_name']
		Category(category_name=category).save()

		return redirect('income:income_categories')
	else:
		return redirect('income:income_categories')

def edit_category(request, category_pk):
	template = 'income/edit-category.html'
	context = {
		'category' : get_object_or_404(Category, pk=category_pk),
	}
	return render(request, template, context)

def update_category(request, category_pk):
	category = get_object_or_404(Category, pk=category_pk)
	if request.method=="POST":
		updated_category = request.POST['category_name']
		category.category_name = updated_category
		category.save()
		return redirect('income:income_categories')
	else:
		return redirect('income:edit_category', category_pk=category_pk)


def delete_category(request, category_pk):
	category = get_object_or_404(Category, pk=category_pk)
	category.delete()
	return redirect('income:income_categories')
