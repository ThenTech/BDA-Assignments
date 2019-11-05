def is_prime(x):
    if x <= 1:
        return False
    if x % 2 == 0 and x != 2:
        return False
    if x % 3 == 0 and x != 3:
        return False
    if x % 5 == 0 and x != 5:
        return False
    if x % 7 == 0 and x != 7:
        return False
    return True

def all_primes_upto(x):
    for i in range(x + 1):
        if is_prime(i):
            print(i)
    return ""



def factorize(x):
    for i in range(1, x):
        if is_prime(i) == True:
            while x % i == 0:
                x = x / i
                print(i)