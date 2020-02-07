from django.urls import path
from .views import profile_view, register_bus_update, update_profile, register_view, login_view, logout_view

app_name='profiles'

urlpatterns = [
    path("profile/<username>", profile_view, name=""),
    path("<username>/bus_registration", register_bus_update, name=""),
    path("accounts/login", login_view, name="login"),
    path("accounts/signup", register_view, name=""),
    path('profile/<username>/update', update_profile, name=""),
    path('accounts/logout', logout_view, name='logout'),
]