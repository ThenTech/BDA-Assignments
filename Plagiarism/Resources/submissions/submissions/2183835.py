import math

def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return True
        else:
            return True
    else:
        return False


def all_primes_upto(x):
    if x > 1:
        for i in range(x):
            if is_prime(i):
                print(i)


def factorize(x):
    while x % 2 == 0:
        print(2),
        x = x / 2

    for i in range(3, int(math.sqrt(x))+1, 2):
        while x % i == 0:
            print(i),
            x = x / i

    if x > 2:
        print(x)