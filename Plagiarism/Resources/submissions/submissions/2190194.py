def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i != 0:
                continue
            return False
        return True
    return False

def all_primes_upto(x):
    b = True
    c = ""
    for j in range(2, x):
        if is_prime(j) == True:
            c = c + str(j) + "\n"
    return c

def factorize(x):
    c = ""
    for j in range(2, x):
        y = x
        if is_prime(j) == True:
            while y%j == 0:
                c = c + str(j) + "\n"
                y = y//j
    return c