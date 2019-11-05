def is_prime(x):
    if x == 1:
        return False
    if x < 0:
        return False
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True

def all_primes_upto(x):
    for i in range(1, x):
        if is_prime(i) == True:
            print(i)

def next_prime(x):
    while is_prime(x) == False:
        x = x + 1
    return x

def factorize(x):
    factor = 2
    while (x != 1):
        while (x % factor == 0):
            print(factor)
            x = x // factor

        factor = next_prime(factor + 1)