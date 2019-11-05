def is_prime(x):
    if x <= 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def all_primes_upto(x):
    for i in range(x+1):
        if is_prime(i):
            print(x)

def factorize(x):
    remainder = x
    i = 0
    for i <= x
        if is_prime(i) and remainder % i == 0
            remainder = remainder // i
            print(i)
        else:
            i += 1
            