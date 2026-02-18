import pytest
from src.task4 import calculate_discount

def test_calculate_discount_formula_basic():

    assert calculate_discount(200, 25) == 150.0

def test_calculate_discount_formula_small_discount():

    assert calculate_discount(50, 1) == pytest.approx(49.5)

def test_calculate_discount_formula_large_price():

    assert calculate_discount(10000, 33) == pytest.approx(6700.0)
