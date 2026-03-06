# Django shortcuts for rendering templates and handling objects
from django.shortcuts import render, get_object_or_404, redirect

# Django authentication decorator
from django.contrib.auth.decorators import login_required

# Django REST Framework components
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Local models and serializers
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


"""
--------------------------------------------------
Template Views (User Interface)
These views render HTML pages using Django templates.
--------------------------------------------------
"""

def movie_list(request):
    """
    Display all available movies on the homepage.
    Movies are ordered by most recent release date.
    """
    movies = Movie.objects.all().order_by("-release_date")
    return render(request, "bookings/movie_list.html", {"movies": movies})


@login_required
def my_bookings(request):
    """
    Display booking history for the currently logged-in user.
    Only bookings belonging to that user are shown.
    """
    bookings = (
        Booking.objects
        .filter(user=request.user)
        .select_related("movie", "seat")  # improves query efficiency
        .order_by("-booking_date")
    )

    return render(request, "bookings/booking_history.html", {"bookings": bookings})


def book_a_seat(request, movie_id):
    """
    Handle seat booking for a specific movie.

    GET request:
        Displays all seats and indicates which ones are already booked.

    POST request:
        Attempts to book the selected seat for the current user.
    """
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id)

        # Check if the seat is already booked for this movie
        already_booked = Booking.objects.filter(movie=movie, seat=seat).exists()

        if not already_booked:
            Booking.objects.create(
                movie=movie,
                seat=seat,
                user=request.user
            )

        return redirect("book_a_seat", movie_id=movie_id)

    # Retrieve all seats ordered by seat number
    seats = Seat.objects.all().order_by("seat_number")

    # Get seat IDs that are already booked for this movie
    booked_seat_ids = Booking.objects.filter(movie=movie).values_list("seat_id", flat=True)

    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "seats": seats,
        "booked_seat_ids": booked_seat_ids,
    })


"""
--------------------------------------------------
API ViewSets (RESTful API)
These provide CRUD endpoints using Django REST Framework.
--------------------------------------------------
"""

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and managing movies.
    Supports full CRUD operations.
    """
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SeatViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing seats and seat availability.
    """
    queryset = Seat.objects.all().order_by('seat_number')
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating and viewing bookings.

    Only authenticated users can create bookings.
    Users can only see their own booking history.
    """
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()

    def get_queryset(self):
        """
        Restrict booking history to the currently logged-in user.
        """
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Prevent duplicate bookings for the same seat in the same movie.
        """
        seat = serializer.validated_data.get('seat')
        movie = serializer.validated_data.get('movie')

        if Booking.objects.filter(movie=movie, seat=seat).exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError("This seat is already booked for this movie.")

        serializer.save(user=self.request.user)