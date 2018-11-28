def fibonacci(n):
    number1 = int(0)
    number2 = int(1)
    count = int(0)
    while count < n:
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
    return nth
