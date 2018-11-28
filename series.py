def fibonacci(n):
    number1 = int(0)
    number2 = int(1)
    count = int(0)
    while count < n:
        if n == 0:
            return 0
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
    return nth


def lucas(n):
    number1 = int(1)
    number2 = int(1)
    count = int(0)
    if n == 0:
        return 0
    while count < n:
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
    return nth

# if __name__ == "__main__"
