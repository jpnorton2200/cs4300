from behave import given, when, then
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from bookings.models import Movie, Seat


@given('there is a movie titled "{title}"')
def step_create_movie(context, title):
    Movie.objects.create(
        title=title,
        description="Test movie",
        release_date="2020-01-01",
        duration=120,
    )


@given('there is a seat numbered {seat_number:d}')
def step_create_seat(context, seat_number):
    Seat.objects.create(seat_number=seat_number)


@given('I am logged in as "{username}" with password "{password}"')
def step_login_user(context, username, password):
    user, created = User.objects.get_or_create(username=username)

    if created:
        user.set_password(password)
        user.save()

    context.client = APIClient()
    context.client.login(username=username, password=password)


@when('I request the movies API')
def step_request_movies(context):
    context.client = APIClient()
    context.response = context.client.get("/api/movies/")


@when('I create a booking for movie "{title}" and seat {seat_number:d}')
def step_create_booking(context, title, seat_number):
    movie = Movie.objects.filter(title=title).first()
    seat = Seat.objects.filter(seat_number=seat_number).first()

    context.response = context.client.post(
        "/api/bookings/",
        {"movie": movie.id, "seat": seat.id},
        format="json"
    )


@then('the response status should be {status_code:d}')
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, (
        f"Expected {status_code}, got {context.response.status_code}"
    )


@then('the movie list should include "{title}"')
def step_check_movie(context, title):
    titles = [movie["title"] for movie in context.response.json()]
    assert title in titles