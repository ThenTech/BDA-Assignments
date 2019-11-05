def is_prime(x):
    if x < 2:
        return False
    y = 0
    for i in range(2, x):
        if x % i == 0:
            y += 1
    if y == 0:
        return True
    else:
        return False

def all_primes_upto(x):
    for i in range(2, x+1):
        if is_prime(i):
            print(i)


def next_prime(x):
    while (not is_prime(x)):
        x = x + 1
    return x

def factorize(x):
    factor = 2
    while (x != 1):
        while(x % factor == 0):
            print(factor)
            x = x // factor
        factor = next_prime(factor + 1)
