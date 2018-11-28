from series import fibonacci
import pytest

def test_single_number():
    """test function which tests by bringing in an even numbered list
    """
    actual = 6
    expected = 8
    assert fibonacci(actual) == expected
