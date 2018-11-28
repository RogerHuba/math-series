from series import fibonacci

def test_single_number():
    """test function which tests by bringing in an even numbered list
    """
    actual = 1
    expected = [1]
    assert fibonacci(actual) == expected
