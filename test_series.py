from series import fibonacci
import pytest

def test_single_number():
    """test function which tests by bringing in an even numbered list
    """
    actual = 5
    expected = 7
    assert fibonacci(actual) == expected
