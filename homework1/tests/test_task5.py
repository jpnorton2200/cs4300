import pytest
from src.task5 import favorite_books, first_three_books, student_database

def test_favorite_books_returns_list():
    assert isinstance(favorite_books(), list)

def test_favorite_books_has_at_least_3():
    assert len(favorite_books()) >= 3

def test_favorite_books_has_title_key():
    assert "title" in favorite_books()[0]

def test_favorite_books_has_author_key():
    assert "author" in favorite_books()[0]

def test_student_database_returns_dict():
    assert isinstance(student_database(), dict)

def test_student_database_contains_bob():
    assert "Bob" in student_database()

def test_student_database_alice_value():
    assert student_database()["Job"] == "1111"
