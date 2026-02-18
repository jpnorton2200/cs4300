import pytest
from src.task7 import vector_dot

def test_vector_dot_basic():
    assert vector_dot([1, 2, 3], [4, 5, 6]) == 32.0

def test_vector_dot_floats():
    assert vector_dot([0.5, 1.5], [2.0, 4.0]) == pytest.approx(7.0)

def test_vector_dot_mismatched_lengths():
    with pytest.raises(ValueError):
        vector_dot([1, 2], [1, 2, 3])
