# Generated by Django 3.0.2 on 2020-02-14 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.IntegerField(default=22)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252)),
                ('images', models.ImageField(default='fixed_pic.jpg', upload_to='events_folder/')),
                ('descriptions', models.TextField(max_length=1330)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='BookingBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hired', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('hired_date', models.DateTimeField(blank=True, null=True)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_app.Directions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'HiringBus',
            },
        ),
    ]