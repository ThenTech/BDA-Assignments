def is_prime(x):
    if x <= 1:
        return False
    
    for i in range(1, x):
        if x % i != 0:
            return False
    return True


def all_primes_upto(x):
    pass


def factorize(x):
    pass