def is_prime(x):
    i = 2
    if i > x:
        return False
    while i < x:
        if x % i == 0:
            return False
        else: 
            i += 1
    return True

def all_primes_upto(x):
    i = 2
    count = 0
    while i <= x:
        for k in range(i):
            if k >= 2 and i % k == 0:
                count += 1
        if count == 0:
            print(i)
        count = 0
        i += 1
                
def factorize(x):
    i = 2
    count = 0
    while i <= x:
        for k in range(i):
            if k >= 2 and i % k == 0:
                count += 1
        if count == 0:
            if x % i == 0:
                print(i)
        count = 0
        i += 1
    