from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from accounts.models import User
from location_app.models import Location, Directions
from core.models import EventType
from .models import HiringBus
from .forms import HiringBForm


def hirebuses(request):
    
    hiring_data = Location.objects.all()
    hiring_info = EventType.objects.all()
    
    if request.method == 'POST':
        hirebus_form = HiringBForm(request.POST)

        if hirebus_form.is_valid():
            event_type = hirebus_form.cleaned_data.get(
                'event_type' 
            )
            needed_amount_of_bus = hirebus_form.cleaned_data.get(
                'how_many_bus_are_needed'
            )
            number_of_sitters = hirebus_form.cleaned_data.get(
                'number_of_sitters'
            )
            particular_location_address = hirebus_form.cleaned_data.get(
                'particular_location_address'
            )
            location_LGA = hirebus_form.cleaned_data.get(
                'location_LGA'
            )
            event_destination_address = hirebus_form.cleaned_data.get(
                'event_destination_address'
            )
            event_LGA = hirebus_form.cleaned_data.get(
                'event_LGA'
            )
            date_and_time = hirebus_form.cleaned_data.get(
                'set_date_and_time'
            )
            hirebus_form = HiringBus.objects.create(

                user=request.user,
                event_type=event_type,
                how_many_bus_are_needed=needed_amount_of_bus,
                number_of_sitters=number_of_sitters,
                particular_location_address=particular_location_address,
                location_LGA=location_LGA,
                event_destination_address=event_destination_address,
                event_LGA=event_LGA,
                set_date_and_time=date_and_time,

            )
            # hirebus_form.instance = request.user
            hirebus_form.save()
            
            return redirect('/home', hirebus_form)
        
    else:
        
        hirebus_form = HiringBForm()
        
    context = {
        
        'hirebus_data': hiring_data,
        
        "hirebus_form": hirebus_form,
        
        'hiring_info': hiring_info
    }
    
    return render(request, 'hiring/hiringforms.html', context)