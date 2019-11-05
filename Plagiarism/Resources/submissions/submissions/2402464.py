def is_prime(x):
    if x < 2:
        return false
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

def factorize(x):
    factor = 2
    while (x != 1):
        while(x % factor == 0):
            print(factor)
            x = x // factor
        factor = next_prime(factor + 1)
