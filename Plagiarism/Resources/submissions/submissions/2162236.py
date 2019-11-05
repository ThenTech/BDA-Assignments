def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            continue
    return True


def all_primes_upto(x):
    for i in range(2, x):
        if is_prime(i):
            print(i)

def factorize(x):
    for i in range(2, x):
        if is_prime(i):
            while x % i == 0:
                print(i)
                x /= i