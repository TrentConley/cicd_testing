"""
Tests for multiplication function.
"""

from math_operations import multiply


def test_multiply_positive_numbers():
    """Test multiplying positive numbers."""
    assert multiply(2, 3) == 6
    assert multiply(10, 5) == 50


def test_multiply_negative_numbers():
    """Test multiplying negative numbers."""
    assert multiply(-5, -3) == 15
    assert multiply(-10, 5) == -50
    assert multiply(10, -5) == -50


def test_multiply_zero():
    """Test multiplying by zero."""
    assert multiply(0, 0) == 0
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0


if __name__ == "__main__":
    test_multiply_positive_numbers()
    test_multiply_negative_numbers()
    test_multiply_zero()
    print("All multiplication tests passed!")
