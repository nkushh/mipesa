from django.shortcuts import render, redirect, get_object_or_404

from .models import ExpenseCategory, ExpenseTransaction

# Create your views here.
def categories(request):
	template = 'expense/categories.html'
	context = {
		'categories' : ExpenseCategory.objects.all().order_by('category_name'),
	}
	return render(request, template, context)

def new_category(request):
	if request.method=="POST":
		category = request.POST['category_name']
		ExpenseCategory(category_name=category).save()

		return redirect('expense:expense_categories')
	else:
		return redirect('expense:expense_categories')

def edit_category(request, category_pk):
	template = 'expense/edit-category.html'
	context = {
		'category' : get_object_or_404(ExpenseCategory, pk=category_pk),
	}
	return render(request, template, context)

def update_category(request, category_pk):
	category = get_object_or_404(ExpenseCategory, pk=category_pk)
	if request.method=="POST":
		updated_category = request.POST['category_name']
		category.category_name = updated_category
		category.save()
		return redirect('expense:expense_categories')
	else:
		return redirect('expense:edit_category', category_pk=category_pk)


def delete_category(request, category_pk):
	category = get_object_or_404(ExpenseCategory, pk=category_pk)
	category.delete()
	return redirect('expense:expense_categories')


# Expense transactions
def new_transaction(request):
	if request.method=="POST":
		category = get_object_or_404(ExpenseCategory, pk=request.POST['category'])
		name = request.POST['name']
		description = request.POST['description']
		amount = request.POST['amount']
		transaction_date = request.POST['transaction_date'] 
		transaction = ExpenseTransaction(category=category, expense_name=name, description=description, amount=amount, transaction_date=transaction_date).save()
		
		return redirect('expense:expense_transactions')
	else:
		return redirect('expense:expense_transactions')

def all_transactions(request):
	template = "expense/transactions.html"
	context = {
		'categories' : ExpenseCategory.objects.all().order_by('category_name'),
		'transactions' : ExpenseTransaction.objects.all(),
	}
	return render(request, template, context)
