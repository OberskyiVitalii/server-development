from django.contrib import admin

from customers.models import Customers

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    pass