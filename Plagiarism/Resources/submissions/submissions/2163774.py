def is_prime (x):
    i = 2
    while x > i:
        if x % i == 0:
            return x % i == 0
        else:
            i += 1
    return x % i == 0

def all_primes_upto(x):
    pass


def factorize(x):
    pass