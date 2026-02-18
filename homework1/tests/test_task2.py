import pytest
from src import task2

def test_get_int():
    val = task2.get_int()
    assert isinstance(val, int)
    assert val == 67

def test_get_float():
    val = task2.get_float()
    assert isinstance(val, float)
    assert val == 3.432

def test_get_string():
    val = task2.get_string()
    assert isinstance(val, str)
    assert val == "Hi World"

def test_get_bool():
    val = task2.get_bool()
    assert isinstance(val, bool)
    assert val == True
