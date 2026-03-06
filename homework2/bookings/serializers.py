from rest_framework import serializers
from .models import Movie, Seat, Booking


"""
--------------------------------------------------
Movie Serializer
Converts Movie model instances into JSON format
and allows them to be created/updated via the API.
--------------------------------------------------
"""

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # Include all movie fields in the API representation
        fields = '__all__'


"""
--------------------------------------------------
Seat Serializer
Used to expose seat information through the API.
Primarily used for checking seat availability.
--------------------------------------------------
"""

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        # Include all seat fields
        fields = '__all__'


"""
--------------------------------------------------
Booking Serializer
Handles booking creation and booking history.

The 'user' field is read-only so the client
cannot assign bookings to another user. Instead,
the logged-in user is automatically attached
inside the BookingViewSet.
--------------------------------------------------
"""

class BookingSerializer(serializers.ModelSerializer):
    # Display the username in API responses
    # but prevent clients from submitting it manually
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Booking

        # Fields included in API responses
        fields = [
            'id',
            'movie',
            'seat',
            'user',
            'booking_date'
        ]

        # Fields that should not be editable by API clients
        read_only_fields = [
            'id',
            'user',
            'booking_date'
        ]