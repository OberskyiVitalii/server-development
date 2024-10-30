from django.contrib import admin

from busses.models import Busses

@admin.register(Busses)
class BussesAdmin(admin.ModelAdmin):
    pass