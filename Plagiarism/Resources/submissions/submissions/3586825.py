def is_prime(x):
    if x <= 1:
        return false
        
    for i in range(2, x):
        if (x % i == 0 and x != i) or x < 0:
            return False
    return True


def all_primes_upto(x):
    pass


def factorize(x):
    pass