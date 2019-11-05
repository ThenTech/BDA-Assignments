def is_prime(isPrime):
    count = 0
    for i in range(1, isPrime):
        if isPrime % i == 0:
            count += 1
    if count == 1:
        return True
    return False


def all_primes_upto(x):
    for i in range(x):
        if is_prime(i):
            print(i)


def next_prime(x):
    while (not is_prime(x)):
        x = x + 1
    return x


def factorize(x):
    factor = 2
    while (x != 1):
        while (x % factor == 0):
            print(factor)
            x = x // factor

        factor = next_prime(factor + 1)