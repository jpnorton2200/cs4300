from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all().order_by("-release_date")
    return render(request, "bookings/movie_list.html", {"movies": movies})

from django.contrib.auth.decorators import login_required

@login_required
def my_bookings(request):
    bookings = (
        Booking.objects
        .filter(user=request.user)
        .select_related("movie", "seat")
        .order_by("-booking_date")
    )
    return render(request, "bookings/booking_history.html", {"bookings": bookings})

def book_a_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id)

        # Booked is now per (movie, seat), not a global seat flag
        already_booked = Booking.objects.filter(movie=movie, seat=seat).exists()

        if not already_booked:
            Booking.objects.create(
                movie=movie,
                seat=seat,
                user=request.user
            )

        return redirect("book_a_seat", movie_id=movie_id)

    seats = Seat.objects.all().order_by("seat_number")

    booked_seat_ids = Booking.objects.filter(movie=movie).values_list("seat_id", flat=True)

    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "seats": seats,
        "booked_seat_ids": booked_seat_ids,
    })

class MovieViewSet(viewsets.ModelViewSet):
    #order the movie by the title
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SeatViewSet(viewsets.ModelViewSet):
    #order seats by their number
    queryset = Seat.objects.all().order_by('seat_number')
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    #user must be logged in
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()

    def get_queryset(self):
        #users can only see their own bookings
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        seat = serializer.validated_data.get('seat')
        movie = serializer.validated_data.get('movie')

        if Booking.objects.filter(movie=movie, seat=seat).exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError("This seat is already booked for this movie.")

        serializer.save(user=self.request.user)