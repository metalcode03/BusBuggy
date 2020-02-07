import datetime

from django.shortcuts import reverse
from django.db import models
from django.db.models import Q

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from location_app.models import Location, Directions
from core.models import BusNumber, EventType






class HiringBus(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    event_type = models.ForeignKey(

        EventType,
        on_delete=models.CASCADE,
        default='others'
    )
    
    how_many_bus_are_needed = models.ForeignKey(

        BusNumber,
        related_name='bus_needed',
        on_delete=models.DO_NOTHING,
        default='1'
    )
    
    number_of_sitters = models.ForeignKey(

        BusNumber,
        on_delete=models.DO_NOTHING,
        default='22'
    )

    particular_location_address = models.CharField(max_length=325)
    location_LGA = models.ForeignKey(Directions, on_delete=models.CASCADE)
    
    event_destination_address = models.CharField(max_length=325)
    event_LGA = models.ForeignKey(Directions, related_name='event_LG', on_delete=models.CASCADE)
    
    set_date_and_time = models.DateTimeField(_("Date_and_time"), blank=True, null=True)
    
    booked_date = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField('date published', auto_now=True)
    
    is_booked = models.BooleanField(default=False)
    
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'BookingBus'
 
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    def __str__(self):
        return self.event_type.name + " by " + self.user.username

    def __unicode__(self):
        return self.event_type.name + " by " + self.user.username

