# Generated by Django 3.0.2 on 2020-02-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('location_img', models.ImageField(blank=True, upload_to='direction_img')),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location_app.Location')),
                ('your_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_locations', to='location_app.Location')),
            ],
            options={
                'verbose_name_plural': 'Directions',
            },
        ),
    ]