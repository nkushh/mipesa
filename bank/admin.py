from django.contrib import admin

from .models import BankAccount, BankTransaction

# Register your models here.
admin.site.register(BankAccount)
admin.site.register(BankTransaction)
