from django.db import models

# Create your models here.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    cleremont_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You should hash and store passwords securely

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Add_Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=255, verbose_name='Vehicle Name')
    celermont_id = models.CharField(max_length=255, verbose_name='Celermont ID')
    groups = models.CharField(max_length=255, verbose_name='Groups')
    zones = models.CharField(max_length=255, verbose_name='Zones')
    current_speed = models.FloatField(verbose_name='Current Speed')
    max_speed = models.FloatField(verbose_name='Max Speed')
    average_speed = models.FloatField(verbose_name='Average Speed')
    distance = models.FloatField(verbose_name='Distance')
    battery = models.FloatField(verbose_name='Battery')
    can_grab_marketplace_jobs = models.BooleanField(verbose_name='Can Grab Marketplace Jobs')
    gps = models.CharField(max_length=255, verbose_name='GPS')
    current_location = models.CharField(max_length=255, verbose_name='Current Location')
    heading_to = models.CharField(max_length=255, verbose_name='Heading To')
    last_connected = models.DateTimeField(verbose_name='Last Connected')
    last_tracked = models.DateTimeField(verbose_name='Last Tracked')
    connection = models.CharField(max_length=255, verbose_name='Connection')
    checked_in_at = models.DateTimeField(verbose_name='Checked In At')
    map = models.CharField(max_length=255, verbose_name='Map')
    action = models.CharField(max_length=255, verbose_name='Action')


    def __str__(self):
        return self.vehicle_name




 

