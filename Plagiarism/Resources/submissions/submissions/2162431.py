def is_prime(x):
    if x % 2 != 0 and x % 3 != 0 and x > 0 and x != 1:
        return True
    elif x == 3 or x == 2:
        return True
    else:
        return False
print(is_prime(3))

def all_primes_upto(x):
    for i in range(x+1):
        if is_prime(i):
            print(i)
    return
print(all_primes_upto(13))

def factorize(x):
    pass