def is_prime(x):
    if x == 1 or x == 0:
        return False
    if x < 0:
        return False
    y = x-1
    while y > 1:
        if x % y == 0:
            return False
        else:
            y -=1
    return True

def all_primes_upto(x):
    for y in range(x):
        if is_prime(y):
            print(y)

def factorize (n):
    i = 2
    while i ** 2 <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            print(i)
    if n > 1:
        print(n)