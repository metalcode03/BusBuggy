from django.urls import path
from . import views

app_name = 'hire'

urlpatterns = [
    path('ordering/form/orderbus', views.hirebuses, name='hirebus'),
]
