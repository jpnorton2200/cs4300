from django.urls import path, include
from .views import SeatViewSet
from .views import MovieViewSet
from .views import BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("seats", SeatViewSet)
router.register("movies", MovieViewSet)
router.register("bookings", BookingViewSet)

urlpatterns = router.urls

