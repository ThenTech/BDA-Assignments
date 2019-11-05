def is_prime(x):
    if x == 1:
        return True
    for i in range(1,x):
        if i != 1 and x%i == 0:
            return False
    return True


def all_primes_upto(x):
    for i in range(1, x+1):
        if is_prime(i):
            print(i)


def factorize(x):
    i = 2
    while x != 1:
        if x % i == 0:
            x /= i
            print(i)
        else:
            i += 1