from django.contrib import admin

from routes.models import Routes

@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    pass