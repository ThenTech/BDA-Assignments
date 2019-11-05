def is_prime(x):
    if x > 1:
        dividable = False
        for i in range(2,x):
            if x%i == 0:
                dividable = True
        if not dividable:
            return True
    return False


def all_primes_upto(x):
    for i in range(2,x+1):
        if is_prime(i):
            print(i)

def factorize(x):
    while x>1:
        for i in range(2, x + 1):
            if is_prime(i) and x % i == 0:
                print(i)
                x = x / i
                break