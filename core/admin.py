from django.contrib import admin
from .models import EventType, BookingBus, BusNumber
# Register your models here.

class BookingBusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'direction')

admin.site.register(EventType)
admin.site.register(BookingBus, BookingBusAdmin)
admin.site.register(BusNumber)

