import pytest
from src.task3 import classify_number, first_n_primes, sum_1_to_100

def test_classify_number_positive():
    assert classify_number(6) == "positive"

def test_classify_number_negative():
    assert classify_number(-9) == "negative"

def test_classify_number_zero():
    """Test that zero is classified as 'zero'."""
    assert classify_number(0) == "zero"

def test_first_10_primes():
    """Test that the first 10 primes are returned correctly."""
    assert first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_1_to_100():
    """Test that the sum of 1 to 100 equals 5050."""
    assert sum_1_to_100() == 5050
