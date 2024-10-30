from django.contrib import admin

from tickets.models import Tickets

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    pass