from django.db import models
from django.contrib.auth.models import User


"""
--------------------------------------------------
Movie Model
Represents a movie that can be booked in the theater.
--------------------------------------------------
"""
class Movie(models.Model):
    # Title of the movie
    title = models.CharField(max_length=100)

    # Short description or summary
    description = models.CharField(max_length=1000)

    # Official release date
    release_date = models.DateField()

    # Duration of the movie in minutes
    duration = models.PositiveIntegerField()

    def __str__(self):
        """
        String representation used in admin panel
        and debugging output.
        """
        return self.title


"""
--------------------------------------------------
Seat Model
Represents a physical seat in the movie theater.
--------------------------------------------------
"""
class Seat(models.Model):
    # Seat number identifier (ex: 1, 2, 3...)
    seat_number = models.PositiveSmallIntegerField()

    def __str__(self):
        """
        Human-readable seat display.
        """
        return f"Seat {self.seat_number}"


"""
--------------------------------------------------
Booking Model
Represents a reservation of a seat for a movie
by a specific user.
--------------------------------------------------
"""
class Booking(models.Model):

    # Movie that the booking is for
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    # Seat being reserved
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    # User who made the booking
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Timestamp of when the booking was created
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Ensure that a seat cannot be booked twice
        for the same movie.
        """
        constraints = [
            models.UniqueConstraint(
                fields=['movie', 'seat'],
                name='unique_movie_seat_booking'
            )
        ]

    def __str__(self):
        """
        Human-readable representation of a booking.
        Useful in Django admin and debugging.
        """
        return f"{self.movie.title} - {self.user.username} - Seat {self.seat.seat_number}"