def is_prime (x):
    i = 2
    while x > i:
        if x % i == 0:
            return not x % i == 0
        else:
            i += 1
    return x % i == 0

def all_primes_upto(x):
    for j in range(2, x):
        if is_prime(j) == bool(true):
            print(j)


def factorize(x):
    pass