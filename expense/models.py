from django.db import models

# Create your models here.
class ExpenseCategory(models.Model):
	category_name = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name

