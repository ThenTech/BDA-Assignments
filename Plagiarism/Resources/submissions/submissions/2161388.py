def is_prime(x):
    if x <= 1:
        False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def all_primes_upto(x):
    for i in range(1, x + 1):
        if is_prime(i):
            print(i)


def factorize(x):
    for i in range(2, x):
        if is_prime(i):
            if x % i == 0:
                print(i)
                x = x / i