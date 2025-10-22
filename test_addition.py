"""
Tests for addition function.
"""

from math_operations import add


def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5
    assert add(10, 20) == 30


def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5


def test_add_zero():
    """Test adding zero."""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5


if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_zero()
    print("All addition tests passed!")
