from django.contrib import messages
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
		if ExpenseCategory.objects.filter(category_name=category).exists():
			messages.error(request, "Error! Category name already exists. Try another!")
			return redirect('expense:expense_categories')
		else:
			ExpenseCategory(category_name=category).save()
			messages.success(request, "Succcess! Category details have been added successfully.")

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
		messages.success(request, "Success! Category details updated successfully.")
		return redirect('expense:expense_categories')
	else:
		return redirect('expense:edit_category', category_pk=category_pk)


def delete_category(request, category_pk):
	category = get_object_or_404(ExpenseCategory, pk=category_pk)
	category.delete()
	messages.success(request, "Success! Category details deleted.")
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
		
		messages.success(request, "Success! Transaction details added successfully.")
		return redirect('expense:expense_transactions')
	else:
		return redirect('expense:expense_transactions')

def all_transactions(request):
	template = "expense/transactions.html"
	context = {
		'categories' : ExpenseCategory.objects.all().order_by('category_name'),
		'transactions' : ExpenseTransaction.objects.all().order_by('-transaction_date'),
	}
	return render(request, template, context)


def edit_transaction(request, transaction_pk):
	template = "expense/edit-transaction.html"
	context = {
		'categories' : ExpenseCategory.objects.all(),
		'transaction' : get_object_or_404(ExpenseTransaction, pk=transaction_pk),
	}

	return render(request, template, context)

def update_transaction(request, transaction_pk):
	transaction = get_object_or_404(ExpenseTransaction, pk=transaction_pk)

	if request.method=="POST":
		transaction.category = get_object_or_404(ExpenseCategory, pk=request.POST['category'])
		transaction.expense_name = request.POST['name']
		transaction.description = request.POST['description']
		transaction.amount = request.POST['amount']
		transaction.transaction_date = request.POST['transaction_date']
		transaction.save()

		messages.success(request, "Success! Transaction details updated successfully.")
		return redirect('expense:expense_transactions')
	else:
		return redirect('expense:edit_transaction', transaction_pk=transaction_pk)


def delete_transaction(request, transaction_pk):
	transaction = get_object_or_404(ExpenseTransaction, pk=transaction_pk)
	transaction.delete()
	messages.success(request, "Success! Transaction details deleted successfully.")
	return redirect('expense:expense_transactions')






