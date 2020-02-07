import datetime

from django.shortcuts import reverse
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from location_app.models import Location, Directions

# Create your models here.

class EventType(models.Model):
    name =  models.CharField(max_length=252)
    images = models.ImageField(upload_to='events_folder/', default='fixed_pic.jpg')
    descriptions = models.TextField(max_length=1330)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name


class BusNumber(models.Model):
    bus_number = models.IntegerField(default=22)
    
    def __str__(self):
        number = self.bus_number
        return str(number)



class BookingBus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE)
    hired = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    hired_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("core:home", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'HiringBus'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.user.username