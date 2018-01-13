from django.db import models

# Create your models here.
class Debt(models.Model):
	amount = models.FloatField()
	balance = models.FloatField()
	debtor = models.CharField(max_length=200)
	description = models.TextField(blank=True, default="")
	taken_on = models.DateField()
	date_due = models.DateField(blank=True, null=True)
	date_recorded = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(default=1)

	def __str__(self):
		return self.debtor

class DebtPayment(models.Model):
	debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
	amount_paid = models.FloatField()
	date_paid = models.DateField()
	date_recorded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.debt.debtor

