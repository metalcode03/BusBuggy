

from django.contrib import admin

from .models import BusRegister, User, Profile

# Register your models here.

admin.site.register(BusRegister)
admin.site.register(User)
admin.site.register(Profile)
