from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all().order_by("-release_date")
    return render(request, "bookings/movie_list.html", {"movies": movies})

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

    def get_queryset(self):
        #users can only see their own bookings
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        seat = serializer.validated_data.get('seat')
        if Booking.objects.filter(seat=seat).exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError("This seat is already booked.")
        serializer.save(user=self.request.user)