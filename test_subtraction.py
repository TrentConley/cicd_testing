"""
Tests for subtraction function.
"""

from math_operations import subtract


def test_subtract_positive_numbers():
    """Test subtracting positive numbers."""
    assert subtract(10, 5) == 5
    assert subtract(20, 8) == 12


def test_subtract_negative_numbers():
    """Test subtracting negative numbers."""
    assert subtract(-5, -3) == -2
    assert subtract(10, -5) == 15


def test_subtract_zero():
    """Test subtracting zero."""
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5


if __name__ == "__main__":
    test_subtract_positive_numbers()
    test_subtract_negative_numbers()
    test_subtract_zero()
    print("All subtraction tests passed!")
