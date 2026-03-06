from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework.test import APIClient
from rest_framework import status

from .models import Movie, Seat, Booking


"""
--------------------------------------------------
Model Tests
These tests verify the core database rules and
relationships between Movie, Seat, and Booking.
--------------------------------------------------
"""

class ModelTests(TestCase):
    def setUp(self):
        """
        Create sample data used in each model test.
        """
        self.user = User.objects.create_user(username="jp", password="pass12345")

        self.movie1 = Movie.objects.create(
            title="Interstellar",
            description="Space movie",
            release_date="2014-11-07",
            duration=169,
        )

        self.movie2 = Movie.objects.create(
            title="Inception",
            description="Dream movie",
            release_date="2010-07-16",
            duration=148,
        )

        self.seat1 = Seat.objects.create(seat_number=1)

    def test_create_booking(self):
        """
        Verify that a booking can be created successfully
        and that it is linked to the correct user, movie, and seat.
        """
        booking = Booking.objects.create(
            user=self.user,
            movie=self.movie1,
            seat=self.seat1
        )

        self.assertEqual(booking.user.username, "jp")
        self.assertEqual(booking.movie.title, "Interstellar")
        self.assertEqual(booking.seat.seat_number, 1)

    def test_same_seat_different_movie_allowed(self):
        """
        Verify that the same seat can be booked for different movies.
        This confirms booking is based on (movie, seat), not seat alone.
        """
        Booking.objects.create(user=self.user, movie=self.movie1, seat=self.seat1)
        booking2 = Booking.objects.create(user=self.user, movie=self.movie2, seat=self.seat1)

        self.assertEqual(booking2.movie.title, "Inception")

    def test_same_seat_same_movie_not_allowed(self):
        """
        Verify that the same seat cannot be booked twice
        for the same movie.
        """
        Booking.objects.create(user=self.user, movie=self.movie1, seat=self.seat1)

        with self.assertRaises(IntegrityError):
            Booking.objects.create(user=self.user, movie=self.movie1, seat=self.seat1)


"""
--------------------------------------------------
API Tests
These tests verify that the REST API endpoints
respond correctly and enforce booking rules.
--------------------------------------------------
"""

class APITests(TestCase):
    def setUp(self):
        """
        Create test users, movies, and seats for API testing.
        Also initialize the API test client.
        """
        self.client = APIClient()

        self.user = User.objects.create_user(username="jp", password="pass12345")
        self.other_user = User.objects.create_user(username="other", password="pass12345")

        self.movie1 = Movie.objects.create(
            title="Movie A",
            description="Description A",
            release_date="2020-01-01",
            duration=100,
        )

        self.movie2 = Movie.objects.create(
            title="Movie B",
            description="Description B",
            release_date="2020-01-02",
            duration=110,
        )

        self.seat1 = Seat.objects.create(seat_number=1)

    def test_list_movies(self):
        """
        Verify that the movies endpoint returns a successful response.
        """
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_booking(self):
        """
        Verify that a logged-in user can create a booking
        through the API.
        """
        self.client.login(username="jp", password="pass12345")

        payload = {
            "movie": self.movie1.id,
            "seat": self.seat1.id
        }

        response = self.client.post("/api/bookings/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_duplicate_booking_same_movie_blocked(self):
        """
        Verify that the API blocks duplicate bookings for
        the same movie and seat.
        """
        self.client.login(username="jp", password="pass12345")

        payload = {
            "movie": self.movie1.id,
            "seat": self.seat1.id
        }

        response1 = self.client.post("/api/bookings/", payload, format="json")
        response2 = self.client.post("/api/bookings/", payload, format="json")

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_same_seat_different_movie_allowed_api(self):
        """
        Verify that the same seat can be booked for different movies
        when using the API.
        """
        self.client.login(username="jp", password="pass12345")

        payload1 = {
            "movie": self.movie1.id,
            "seat": self.seat1.id
        }

        payload2 = {
            "movie": self.movie2.id,
            "seat": self.seat1.id
        }

        response1 = self.client.post("/api/bookings/", payload1, format="json")
        response2 = self.client.post("/api/bookings/", payload2, format="json")

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_booking_history_only_shows_current_user_bookings(self):
        """
        Verify that users only see their own booking history
        from the bookings endpoint.
        """
        Booking.objects.create(user=self.other_user, movie=self.movie1, seat=self.seat1)

        self.client.login(username="jp", password="pass12345")
        response = self.client.get("/api/bookings/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)