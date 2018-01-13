from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Debt, DebtPayment

# Create your views here.
def new_debt(request):
	if request.method=="POST":
		amount = request.POST['amount']
		debtor = request.POST['debtor']
		description = request.POST['description']
		taken_on = request.POST['taken_on']
		date_due = request.POST['date_due']

		Debt(amount=amount, balance = amount, debtor=debtor, description=description, taken_on=taken_on, date_due=date_due).save()
		messages.success(request, "Success! Debt records successfully added.")
		return redirect('debts:debts_list')
	else:
		return redirect('debts:debts_list')

def debt_list(request):
	template = "debts/debts-list.html"
	context = {
		'debts' : Debt.objects.filter(status=1).order_by('-taken_on'),
	}

	return render(request, template, context)


def update_debt(request, debt_pk):
	debt = get_object_or_404(Debt, pk=debt_pk)

	if request.method=="POST":
		debt.amount = request.POST['amount']
		debt.balance = request.POST['balance']
		debt.debtor = request.POST['debtor']
		debt.description = request.POST['description']
		debt.taken_on = request.POST['taken_on']
		debt.date_due = request.POST['date_due']

		debt.save()
		messages.success(request, "Success! Debt details updated successfully.")
		return redirect('debts:debts_list')
	else:
		template = "debts/edit-debt.html"
		context = {
			'debt' : debt,
		}
		return render(request, template, context)


def delete_debt(request, debt_pk):
	debt = get_object_or_404(Debt, pk=debt_pk)
	debt.delete()
	messages.success(request, "Success! Debt details deleted successfully.")
	return redirect('debts:debts_list')


def make_payment(request, debt_pk):
	debt = get_object_or_404(Debt, pk=debt_pk)

	if request.method=="POST":
		debt = debt
		amount_paid = request.POST['amount']
		date_paid = request.POST['date_paid']

		debt.balance = debt.balance - float(amount_paid)
		if debt.balance < 1:
			debt.status = 0

		debt.save()

		DebtPayment(debt=debt, amount_paid=amount_paid, date_paid=date_paid).save()
		messages.success(request, "Success! Debt payment has been recorded.")
		return redirect('debts:debts_list')
	else:
		template = "debts/pay.html"
		context = {
			'debt' : debt,
		}
		return render(request, template, context)
