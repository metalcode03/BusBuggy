from webbrowser import register

from django.contrib import admin

from .models import Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'state', 'city', 'country')

admin.site.register(Location, LocationAdmin)