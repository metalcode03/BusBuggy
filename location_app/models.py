from django.db import models





class Location(models.Model):
    
    # longtitude = models.IntegerField()
    # lagtitude = models.IntegerField()

    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    # ip = models.GenericIPAddressField()

    def __str__(self):
        return self.address
    # + ", " + self.city + ", " + self.state



class DirectionManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
               Q(title__icontains=query)
            #    Q(your_location=query)
            #    Q(destination__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs



class Directions(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    location_img = models.ImageField(upload_to='direction_img', blank=True)
    discount_price = models.FloatField(blank=True, null=True)
    your_location = models.ForeignKey(Location, related_name='user_locations', on_delete=models.DO_NOTHING)
    destination = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    slug = models.SlugField()
    
    objects = DirectionManager()
    
    class Meta:
        verbose_name_plural = 'Directions'
    
    def __str__(self):
        return self.title
    
    def get_add_to_bookings_url(self):
        return reverse(
        "core:addhire",
        kwargs= {
            "slug":self.slug
        }
    )
    def get_absolute_url(self):
        return reverse("core:direction_detail", kwargs={
            "pk": self.pk,
            "slug":self.slug
        })