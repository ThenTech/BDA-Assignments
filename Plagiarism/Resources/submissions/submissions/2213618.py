def is_prime(x):
    if x > 1:
        for i in range(1, x):
            if x % i == 0:
                return False
            else:
                return True
    return False

def all_primes_upto(x):
    pass


def factorize(x):
    pass