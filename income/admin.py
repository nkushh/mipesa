from django.contrib import admin

from .models import Category, IncomeTransaction

# Register your models here.
admin.site.register(Category)
admin.site.register(IncomeTransaction)
