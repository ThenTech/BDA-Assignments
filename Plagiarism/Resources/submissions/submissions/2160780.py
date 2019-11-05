import math


def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False


def all_primes_upto(x):
    for num in range(x):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


def factorize(x):
    while x % 2 == 0:
        print(2)
        x /= 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            print(i)
            x /= i
    if x > 2:
        print(x)


print(factorize(128))
