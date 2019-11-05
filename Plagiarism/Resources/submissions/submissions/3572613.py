def is_prime(x):
    for i in range(2, x):
        if int((x//i)*i) == x:
            return false
    return true


def all_primes_upto(x):
    for i in range(2, x+1):
        if is_prime(i):
            print(i)


def factorize(x):
    for i in range(2, x+1):
        if is_prime(i) and int((x//i)*i) == x:
            x = int(x//i)
            print(i)