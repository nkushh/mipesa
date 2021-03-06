from django.db import models

# Create your models here.
class ExpenseCategory(models.Model):
	category_name = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name

class ExpenseTransaction(models.Model):
	category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
	expense_name = models.CharField(max_length=200)
	description = models.TextField(blank=True, default="")
	amount = models.FloatField()
	transaction_date = models.DateField()
	date_recorded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.expense_name

