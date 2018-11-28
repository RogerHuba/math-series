from series import fibonacci

def test_single_number():
    """test function which tests by bringing in an even numbered list
    """
    actual = 4
    expected = 3
    assert fibonacci(actual) == expected
