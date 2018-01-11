from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import SaccoAccount, SaccoTransaction

# Create your views here.
def new_account(request):
	if request.method=="POST":
		sacco = request.POST['sacco_name']
		account_name = request.POST['account_name']
		account_type = request.POST['account_type']
		account_no = request.POST['account_no']
		balance = request.POST['balance']
		date_created = request.POST['date_created']

		if SaccoAccount.objects.filter(account_no=account_no).exists():
			messages.error(request, "Error! The Account Number entered already exists.")
			return redirect('sacco:sacco_accounts')
		else:
			account = SaccoAccount(sacco_name=sacco, account_name=account_name, account_type=account_type, account_no=account_no, balance=balance, date_created=date_created).save()
			messages.success(request, "Success! Account details entered successfully.")
			return redirect('sacco:sacco_accounts')
	else:
		return redirect('sacco:sacco_accounts')

def all_accounts(request):
	template = "sacco/accounts.html"
	context = {
		'accounts' : SaccoAccount.objects.all().order_by('account_name'),
	}

	return render(request, template, context)

def edit_account(request, account_pk):
	template = "sacco/edit-account.html"
	context = {
		'account' : get_object_or_404(SaccoAccount, pk=account_pk),
	}

	return render(request, template, context)

def update_account(request, account_pk):
	account = get_object_or_404(SaccoAccount, pk=account_pk)

	if request.method=="POST":
		account.sacco_name = request.POST['sacco_name']
		account.account_name = request.POST['account_name']
		account.account_type = request.POST['account_type']
		account.account_no = request.POST['account_no']
		account.balance = request.POST['balance']
		account.date_created = request.POST['date_created']
		account.save()

		messages.success(request, "Success! Account details have been updated.")
		return redirect('sacco:sacco_accounts')
	else:
		return redirect('sacco:edit_account', account_pk=account_pk)

def delete_account(request, account_pk):
	account = get_object_or_404(SaccoAccount, pk=account_pk)
	account.delete()
	messages.success(request, "Success! Account has been deleted.")
	return redirect('sacco:sacco_accounts')

# Transactions methods

def new_transaction(request):
	if request.method=="POST":
		account = get_object_or_404(SaccoAccount, pk=request.POST['account'])
		transaction_type = request.POST['transaction_type']
		description = request.POST['description']
		amount = request.POST['amount']
		transaction_date = request.POST['transaction_date'] 

		if transaction_type=="Deposit":
			account.balance = account.balance + float(amount)
			account.save()
		elif transaction_type=="Withdraw":
			if account.balance < amount:
				messages.error(request, "Error! Your withdrawal request exceeds your account balance")
				return redirect('sacco:sacco_transactions')
			else:
			 	account.balance = account.balance - float(amount)
			 	account.save()

		transaction = SaccoTransaction(account=account, transaction_type=transaction_type, description=description, amount=amount, transaction_date=transaction_date).save()
		
		messages.success(request, "Success! {} transaction successfully recorded".format(transaction_type))
		return redirect('sacco:sacco_transactions')
	else:
		return redirect('sacco:sacco_transactions')

def all_transactions(request):
	template = "sacco/transactions.html"
	context = {
		'accounts' : SaccoAccount.objects.all().order_by('account_name'),
		'transactions' : SaccoTransaction.objects.all().order_by('-transaction_date'),
	}
	return render(request, template, context)

def edit_transaction(request, transaction_pk):
	template = "sacco/edit-transaction.html"
	context = {
		'accounts' : SaccoAccount.objects.all().order_by('account_name'),
		'transaction' : get_object_or_404(SaccoTransaction, pk=transaction_pk),
	}

	return render(request, template, context)

def update_transaction(request, transaction_pk):
	transaction = get_object_or_404(SaccoTransaction, pk=transaction_pk)

	if request.method=="POST":
		transaction.account = get_object_or_404(SaccoAccount, pk=request.POST['account'])
		transaction.transaction_type = request.POST['transaction_type']
		transaction.description = request.POST['description']
		transaction.amount = request.POST['amount']
		transaction.transaction_date = request.POST['transaction_date']
		transaction.save()
		messages.success(request, "Success! Transaction details successfully updated")
		return redirect('sacco:sacco_transactions')
	else:
		return redirect('sacco:edit_transaction', transaction_pk=transaction_pk)


def delete_transaction(request, transaction_pk):
	transaction = get_object_or_404(SaccoTransaction, pk=transaction_pk)
	transaction.delete()
	return redirect('sacco:sacco_transactions')

def fetch_account(request, account_pk):
	template = "sacco/account.html"
	context = {
		'account' : get_object_or_404(SaccoAccount, pk=account_pk),
	}

	return render(request, template, context)










