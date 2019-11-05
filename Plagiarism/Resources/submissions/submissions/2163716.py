def is_prime(x):
    for i in range(2, 10):
        if x != i and x % i == 0 or x <= 1:
            return False
    return True

def all_primes_upto(x):
    for i in range(0, x):
        if is_prime(i):
            print(i)


def factorize(x):
    i = 0
    while x > 1:
        while is_prime(i) and x % i == 0:
            print(i)
            x /= i
        i += 1