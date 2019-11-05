def is_prime(x):
    numbers = "23456789"

    for number in numbers:
        number = int(number)
        if x != number:
            if x % number == 0 or x <= 1:
                return False

        if number == 9:
            return True

def all_primes_upto(x):
    for i in range(0, x):
        if is_prime(i):
            print(i)

def factorize(x):
    i = 0
    while x > 1:
        while is_prime(i) and x % i == 0:
            print(i)
            x /= i
        i += 1