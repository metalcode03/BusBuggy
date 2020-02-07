# Create your views here.
from os.path import exists

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.db import transaction
from django.shortcuts import redirect, render
from django.template.loader import get_template

# from accounts.models import User
from .forms import (BusRegisterForm, ProfileForm, UserLoginForm,
                    UserRegistrationForm)
from .models import BusRegister, User


def register_view(request, *args, **kwargs):
    next = request.GET.get('next')
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        # template = get_template('success_email.txt')
        # email = request.user.get('email')
        # content = {
        #     'username':request.user.get('username'),
        #     'email':request.user.get('email')
        # }
        # content = template.render(content)

        # email = EmailMessage(
        #     'Success Now Registration Complete',
        #     content,
        #     'BusBuggy',
        #     [email]
        # )
        if next:
            return redirect(next)
        return redirect('/home')
    context = {
        'forms': form,
    }
    return render(request, 'registration/register_user.html', context)


def login_view(request, *args, **kwargs):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        if next:
            return redirect(next)
        return redirect('/home')
    context = {
        'forms': form
    }
    return render(request, 'registration/login_user.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login')


@login_required
@transaction.atomic
def update_profile(request, username):
    username = User.objects.get(username=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request,
                'Your Profile was successfully updated!!'
            )
            return redirect('/profile/%s' % username)
        else:
            messages.error(request, 'please correct the error below.')
    else:
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'main_profile/profile_edit.html', {'profile_form': profile_form})


@login_required
def profile_view(request, username):
    username = User.objects.get(username=username)
    user_view = User.objects.filter(username=username)

    context = {
        'username': user_view
    }
    return render(request, 'main_profile/profile_view.html', context)


def empty_strings(request):
    return redirect(request, '/home')


@login_required
def register_bus_update(request, username):
    username = User.objects.get(username=request.user)
    if request.method == 'POST':
        bus_register_form = BusRegisterForm(
            request.POST, request.FILES)

        if bus_register_form.is_valid():
            # bus_register_form.instance = request.user
            bus_picture_data = bus_register_form.cleaned_data.get('picture_of_bus')
            numbered_sit_data = bus_register_form.cleaned_data.get('number_of_sits')
            plate_number_data = bus_register_form.cleaned_data.get('bus_plate_number')
            data_qs = BusRegister.objects.filter(bus_plate_number=plate_number_data)
            if data_qs.exists():
                messages.error(
                    request,
                    'This plate number is already registered, please check correctly!!'
                )
                return redirect('./bus_registration')
            location_data = bus_register_form.cleaned_data.get('location')
            agreement_data = bus_register_form.cleaned_data.get('agreement')
            pleaseGod = BusRegister.objects.create(
                user=request.user,
                picture_of_bus=bus_picture_data,
                bus_plate_number=plate_number_data,
                number_of_sits=numbered_sit_data,
                location=location_data,
                agreement=agreement_data
             )
            pleaseGod.save()
            # bus_register_form.save()
            
            messages.success(
                request,
                'Your Bus was successfully Registered!!'
            )
            return redirect('/profile/%s' % username)
        # else:
        #     messages.error(request, 'please correct the error below.')
    else:
        profile_form = BusRegisterForm()
    return render(request, 'main_profile/profile_edit.html', {'profile_form': profile_form})


def logout_view(request):
    logout(request)
    messages.info(request, 'you have sucessfully logged out')
    return redirect('/home')