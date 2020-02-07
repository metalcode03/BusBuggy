

from django.contrib import admin

from .models import BusRegister, User

# Register your models here.

admin.site.register(BusRegister)
admin.site.register(User)
