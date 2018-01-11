from django.db import models

# Create your models here.
class BankAccount(models.Model):
	bank_name = models.CharField(max_length=200)
	account_name = models.CharField(max_length=200)
	account_type = models.CharField(max_length=200, blank=True, default="")
	account_no = models.CharField(max_length=20)
	balance = models.FloatField(default=0)
	date_created = models.DateField()
	added_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(default=1)

	def __str__(self):
		return "{} - {}".format(self.account_name, self.bank_name)

class BankTransaction(models.Model):
	account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
	transaction_type = models.CharField(max_length=20)
	description = models.TextField(blank=True, default="")
	amount = models.FloatField()
	transaction_date = models.DateField()
	date_recorded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.transaction_type
