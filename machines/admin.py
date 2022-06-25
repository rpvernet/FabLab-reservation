from django.contrib import admin

# Register your models here.
from .models import Machine

class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Machine, MachineAdmin)

