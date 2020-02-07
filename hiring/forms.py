from django import forms
from .models import HiringBus

class HiringBForm(forms.ModelForm):
    
    class Meta:
        model = HiringBus
        fields = [
            'event_type',
            'how_many_bus_are_needed',
            'number_of_sitters',
            'particular_location_address',
            'location_LGA',
            'event_destination_address',
            'event_LGA',
            'set_date_and_time',
        ]