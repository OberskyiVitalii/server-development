from django.contrib import admin

from drivers.models import Drivers

@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    pass