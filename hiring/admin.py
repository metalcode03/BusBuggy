from django.contrib import admin
from .models import HiringBus
# Register your models here.

class HiringBusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event_type', 'particular_location_address', 'event_destination_address')

admin.site.register(HiringBus, HiringBusAdmin)