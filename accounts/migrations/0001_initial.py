# Generated by Django 3.0.2 on 2020-02-14 17:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contain number', regex='^[a-zA-Z0.+-]*$')])),
                ('email', models.EmailField(max_length=300, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=228, verbose_name='password')),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('bus_driver', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(default=234)),
                ('image', models.ImageField(default='avatar.jpg', upload_to='profile_img/')),
                ('sex', models.CharField(choices=[('MA', 'Male'), ('FA', 'Female'), ('OT', 'Others')], default=('OT', 'Others'), max_length=10)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location_app.Location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_of_bus', models.ImageField(default='default.jpg', upload_to='bus_profile/')),
                ('bus_plate_number', models.CharField(max_length=100)),
                ('number_of_sits', models.IntegerField(default=22)),
                ('agreement', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location_app.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]