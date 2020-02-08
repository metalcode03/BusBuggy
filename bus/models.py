from django.db import models
from accounts.models import BusRegister
from core.models import BookingBus
from hiring.models import HiringBus

# Create your models here.


class Notifcation(models.Model):
    user = models.OneToOneField(BusRegister, on_delete=models.CASCADE)
    message = models.CharField(max_length=350)
    date = models.DateTimeField(auto_now_add=True)
    
# @receiver
# (post_save, sender=Model)
# def _post_save_receiver(sender, **kwargs):
    

