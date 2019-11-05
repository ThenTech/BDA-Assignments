def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x / i == x // i:
                return False
        return True
    else:
        return False


def all_primes_upto(x):
    for i in range(x+1):
        if is_prime(i):
            print(i)


def factorize(x):
    def is_prime_and_divisible(x, i):
        if is_prime(i) and (x / i == x // i):
            x /= i
            print(i)
            is_prime_and_divisible(x, i)
    for i in range(x):
        is_prime_and_divisible(x, i)
