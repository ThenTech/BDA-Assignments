def is_prime(x):
    numbers = "23456789"

    for number in numbers:
        number = int(number)
        if x != number:
            if x % number == 0 or x <= 1:
                return False

        if number == 9:
            return True
