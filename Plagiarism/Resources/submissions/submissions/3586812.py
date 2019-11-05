def is_prime(x):
    for i in range(1, x):
        if (x % i == 0 and x != i) or x < 0:
            return False
    return True


def all_primes_upto(x):
    pass


def factorize(x):
    pass