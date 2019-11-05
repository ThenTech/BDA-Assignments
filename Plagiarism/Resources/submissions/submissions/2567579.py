def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True

    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


def all_primes_upto(x):
    for k in range(2, x + 1):
        if is_prime(k):
            print(k)


def factorize(x):
    primes = [k for k in range(2, x + 1) if is_prime(k)]
    while x > 1:
        for p in primes:
            if x % int(p) == 0:
                print(p)
                x = x / int(p)
