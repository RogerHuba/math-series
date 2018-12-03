import sys


def fibonacci(n):
    """Generate the nth number of the fib sequence"""
    number1 = 0
    number2 = 1
    count = 2

    if type(n) is not int or n < 0:
        raise TypeError('Please enter a positive number')

    if n == 0 or n == 1:
        return n
    while count < n + 1:
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
    return nth


def lucas(n):
    """Generate the nth instance of the lucas
    """
    number1 = 1
    number2 = 2
    nth = 1

    if type(n) is not int:
        raise TypeError('Please enter a number')

    if n == 0:
        return 2
    if n == 1:
        return 1
    for count in range(2, n + 1):
        nth = number1 + number2
        number2 = number1
        number1 = nth
    return nth


if __name__ == "__main__":
    print(fibonacci(4))
    print (lucas(4))
    sys.exit()
