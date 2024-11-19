from django.contrib import admin

from routes.models import Stop

@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    pass