def is_prime(x):
    if x > 2:
        for i in range(2, x-1):
            if x % i == 0:
                return False
        return True
    elif x == 2:
        return True
    else:
        return False

print(is_prime(4))

def all_primes_upto(x):
    all_primes = []
    for i in range(x):
        if is_prime(i):
            all_primes.append(i)
            print(i)

def factorize(x):
    pass