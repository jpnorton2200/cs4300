from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    release_date = models.DateField()
    duration = models.DecimalField(max_digits = 4, decimal_places = 1)

class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.BooleanField(default=False)

class Booking(models.Model):
    movie = models.CharField(max_length = 100)    
    seat = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()