def is_prime (x):
    i = 2
    while x > i:
        if x % i == 0:
            return not x % i == 0
        else:
            i += 1
    return x % i == 0

def all_primes_upto(x):
    leeg = ""
    for j in range(x):
        if is_prime(j):
            leeg += j
    return leeg



def factorize(x):
    pass