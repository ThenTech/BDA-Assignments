def is_prime(x):
    if x > 2:
        for i in range(2, x-1):
            if x % i == 0:
                return False
            else:
                return True
    elif x == 2:
        return True
    else:
        return False

def all_primes_upto(x):
    pass


def factorize(x):
    pass