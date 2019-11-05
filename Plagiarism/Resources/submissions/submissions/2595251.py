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
def next_prime(x):
    while not is_prime:
        x = x+1
    return x 
def factorize(x):
    deler = 2
    while (x % deler == 0):
        print(deler)
        x /= deler  
    deler = next_prime(deler+1)
        
            