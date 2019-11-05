def is_prime(x):
    priem = True
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return priem

def all_primes_upto(x):
    for i in range(2, x+1):
        if is_prime(i):
            print(i) 

def factorize(x):
    for i in [all_primes_upto(x)]:
        while x % i == 0:
            print(i)
            x /= i
        
            