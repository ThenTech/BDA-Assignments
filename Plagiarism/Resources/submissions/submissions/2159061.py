def is_prime(x):
    for i in range(1, x):
        if x % i == 0 and x != i and x != 1:
            return True
    return False

def all_primes_upto(x):
    pass


def factorize(x):
    pass