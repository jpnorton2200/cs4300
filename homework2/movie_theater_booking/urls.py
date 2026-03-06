"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from bookings.views import movie_list
from bookings.views import movie_list, book_a_seat
from django.urls import include, path
from bookings import views as booking_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_list, name='movie_list'),
    path("api/", include("bookings.apis")),
    path("movies/<int:movie_id>/book/", book_a_seat, name="book_a_seat"),
    path("my-bookings/", booking_views.my_bookings, name="my_bookings"),
]
