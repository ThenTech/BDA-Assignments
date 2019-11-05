def is_prime(x):
    priem = True
    if x < 2:
        return False
    for i in range(2,x):
        if x % i != 0:
            return False
    return True


def all_primes_upto(x):
    pass


def factorize(x):
    pass