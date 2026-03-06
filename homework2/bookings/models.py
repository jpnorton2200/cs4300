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

    def __str__(self):
        return f"Seat {self.seat_number}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'seat'], name='unique_movie_seat_booking')
        ]

    def __str__(self):
        return f"{self.movie.title} - {self.user.username} - Seat {self.seat.seat_number}"