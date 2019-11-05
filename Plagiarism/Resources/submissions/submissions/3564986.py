def is_prime(x):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def all_primes_upto(x):
    pass


def factorize(x):
    pass