from django.contrib import admin

from .models import Debt, DebtPayment

# Register your models here.
admin.site.register(Debt)
admin.site.register(DebtPayment)
