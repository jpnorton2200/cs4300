"""
--------------------------------------------------
API Routing Configuration
This file defines the REST API endpoints for the
Movie Theater Booking application using Django
REST Framework routers.
--------------------------------------------------
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import ViewSets that provide API functionality
from .views import MovieViewSet, SeatViewSet, BookingViewSet


"""
--------------------------------------------------
Router Configuration
The DefaultRouter automatically generates standard
RESTful routes for each ViewSet.
--------------------------------------------------
"""

router = DefaultRouter()

# Register API endpoints
router.register("movies", MovieViewSet)
router.register("seats", SeatViewSet)
router.register("bookings", BookingViewSet)


"""
--------------------------------------------------
URL Patterns
Expose the automatically generated router URLs.
These will be included in the main project urls.py
under the /api/ path.
--------------------------------------------------
"""

urlpatterns = router.urls

