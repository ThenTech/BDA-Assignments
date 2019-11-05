def is_prime(x):
    if x == 2 or x == 3 or x == 7 or x == 5:
        return True
    elif x > 2 and not(x % 2 == 0 or x % 3 == 0 or x % 7 == 0 or x % 5 == 0):
        return True
    else:
        return False

def all_primes_upto(x):
    i = 0
    while i <= x:
        if is_prime(i):
            print(i)
        i += 1

def factorize(x):
    i = 0
    maal = 1
    while maal != x:
        while i <= x:
            if is_prime(i):
                maal *= i
            i += 1