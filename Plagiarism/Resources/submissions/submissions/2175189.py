def is_prime(x):
    bool = True
    for i in range(2, x):
        if x % i == 0:
            bool = False
            break
    return bool


def all_primes_upto(x):
    for i in range(0, x+1):
        if is_prime(i):
            print(i)


def factorize(x):
    i = 2
    while i <= x:
        if x % i == 0:
            print(i)
            x = x / i
        else:
            i = i + 1
