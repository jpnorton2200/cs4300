from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    release_date = models.DateField()
    #minutes of movie, ie 60, 90, 180, etc.
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.PositiveSmallIntegerField()
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seat_number)

class Booking(models.Model):
    #many bookings can happen for one movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #only one booking can happen for this seat
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    #one user can make many bookings
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie + " - " + self.user + " - " + self.seat