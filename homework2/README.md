Movie Theater Booking Application
Overview

This project is a RESTful Movie Theater Booking Application built using Django and Django REST Framework. The application allows users to view available movies, book seats, and view their booking history through both a REST API and a Bootstrap-based user interface.

The system demonstrates the use of Django's Model–View–Template (MVT) architecture along with RESTful API development, automated testing, and deployment.

Features
Movie Listings

Users can view available movies including:

Title

Description

Release date

Duration

Movies are available through:

/api/movies/

and through the web interface.

Seat Booking

Users can book seats for a movie. The application ensures that:

A seat can only be booked once per movie

The same seat can be booked for different movies

Booking endpoint:

/api/bookings/
Booking History

Users can view their personal booking history.

Web interface:

/my-bookings/

API endpoint:

/api/bookings/

The API only returns bookings belonging to the authenticated user.

Technologies Used

Python

Django

Django REST Framework

Bootstrap

SQLite (local development)

PostgreSQL (Render deployment)

Behave (BDD testing)

Gunicorn

WhiteNoise

Project Structure
homework2/
│
├── bookings/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   ├── apis.py
│   └── templates/
│       └── bookings/
│           ├── base.html
│           ├── movie_list.html
│           ├── seat_booking.html
│           └── booking_history.html
│
├── features/
│   ├── booking.feature
│   └── steps/
│       └── booking_steps.py
│
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── requirements.txt
├── build.sh
└── manage.py
Installation and Setup
1. Clone the repository
git clone <repo-url>
cd homework2
2. Create a virtual environment
python3 -m venv myenv
source myenv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py migrate
5. Create an admin user
python manage.py createsuperuser
6. Start the server
python manage.py runserver 0.0.0.0:3000

Access the application through the DevEdu App link.

API Endpoints
Movies
GET /api/movies/
POST /api/movies/
Seats
GET /api/seats/
Bookings
GET /api/bookings/
POST /api/bookings/
Testing

The application includes several types of automated tests.

Unit Tests

Run using:

python manage.py test

Tests verify:

model constraints

booking rules

seat availability

Behavior Driven Development (BDD)

BDD scenarios are implemented using Behave.

Run with:

behave

Example scenarios:

Viewing available movies

Creating a booking through the API

Deployment

The application is deployed using Render.

Deployment configuration includes:

PostgreSQL database

Gunicorn application server

WhiteNoise static file handling

environment variable configuration

A build.sh script is used to:

pip install dependencies
run migrations
collect static files
AI Usage Disclosure

AI tools were used during the development of this project to assist with:

debugging Django configuration issues

understanding REST framework implementation

improving code structure and documentation

generating example test scenarios and explanations

AI assistance was used as a learning aid, and all generated content was reviewed, tested, and modified before inclusion in the final project. ChatGPT was used to write some final pieces such as the tests, as well as the booking page html and related files.
Author

JP Norton
CS4300
University of Colorado Colorado Springs

License

This project is for academic use only.