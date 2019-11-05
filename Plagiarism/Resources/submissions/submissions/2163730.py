def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    i = 2
    while i <= x:
        if x % i == 0 and i != x:
            return False
        else:
            i = i+1
        if i == x:
            return True

def all_primes_upto(x):
    for i in range(2,x):
        if is_prime(i):
            print(i)

def factorize(x):
    i = 2
    while i <= x:
        if x % i == 0:
            print(i)
            x = x/i
            continue
        else:
            i = i+1