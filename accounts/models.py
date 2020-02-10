from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager)
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from location_app.models import Location

# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0.+-]*$'

# USER MAINTAINANCE CLASS


class UserManager(BaseUserManager):

    # HANDLING MAIN USER MANAGEMENT

    def create_user(self, username, email, password=None):

        if not email:
            ValueError('User must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.active = True

        user.save()

        return user

    # HANDLING SUPERUSER MANAGEMENT WHICH IS THE ADMIN

    def create_superuser(self, username, email, password=None):

        user = self.create_user(
            username,
            email,
            password=password
        )

        user.admin = True
        user.staff = True
        user.active = True
        user.bus_driver = True

        user.save()

        return user

    # HANDLING STAFF USER MANAGEMENT

    def create_staffuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password
        )

        user.staff = True
        user.active = True
        user.bus_driver = True

        user.save()

        return user

    # HANDLING BUS USER MANAGEMENT

    def create_bususer(self, username, email, password=None):

        user = self.create_user(
            username,
            email,
            password=password
        )

        user.active = True
        user.bus_driver = True

        user.save()

        return user


# USER MAIN CLASS MODELS
class User(AbstractBaseUser):
    
    SEXCHOICE = (
        ('MA', _('Male')),
        ('FA', _('Female')),
        ('OT', _('Others'))
    )

    # MAIN USER LOGIN AND SIGNUP
    username = models.CharField(

        max_length=200,

        unique=True,

        validators=[

            RegexValidator(

                regex=USERNAME_REGEX,

                message='Username must be alphanumeric or contain number',

                code='invalid_username'

            )
        ]
    )

    email = models.EmailField(

        max_length=300,

        unique=True,

        verbose_name='email address'

    )

    # FOR MAIN PROFILE ACCESS
    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    phone_number = models.IntegerField(default=+234)

    image = models.ImageField(upload_to='profile_img/', default='avatar.jpg')

    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    sex = models.CharField(
        max_length=2,
        choices=SEXCHOICE,
        default=SEXCHOICE[2]
    )
    password = models.CharField(_('password'), max_length=228)

    # FOR VERIFICATION AND PERMISSION
    active = models.BooleanField(default=True)

    admin = models.BooleanField(default=False)

    staff = models.BooleanField(default=False)

    bus_driver = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email

    def get_long_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_bus_driver(self):
        return self.bus_driver


class BusRegister(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_of_bus = models.ImageField(
        
        upload_to='bus_profile/',
        
        default='default.jpg'
        
        )
    bus_plate_number = models.CharField(
        
        max_length=100,
        
        default=models.NOT_PROVIDED
        
    )
    
    number_of_sits = models.IntegerField(default=22)
    
    location = models.ForeignKey(
        
        Location,
        
        on_delete=models.DO_NOTHING
    )
    
    # location = models.CharField(max_length=150, default=NOT_PROVIDED, blank=True)
    
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
