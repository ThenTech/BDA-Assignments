def is_prime(x):
    if x <= 1:
        return False
        
    for i in range(2, x):
        if (x % i == 0 and x != i) or x < 0:
            return False
    return True


def all_primes_upto(x):
    for i in range(x):
        if (is_prime(i)):
            print(i)


def factorize(x):
    i = 2
    while (x != 1):
        if is_prime(i):
            if x % i == 0:
                print(i)
                x = x / i
            else:
                i += 1
        else:
            i += 1
            
            
            