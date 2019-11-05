def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0 and x != i:
                return False
        return True
    return False

def all_primes_upto(x):
    for i in range(1, x):
        if is_prime(i) == True:
            print(i)


def factorize(x):
    remaining = x
    
    while remaining > 1:
        for i in range(2, remaining):
            if is_prime(i) and remaining % i == 0:
                print(i)
                remaining = remaining / i
                break
            