def is_prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def all_primes_upto(x):
    for i in range(0,x):
        if is_prime(i):
            print(i)


def factorize(x):
    for i in range(1,x):
        teller = i
        while is_prime(teller):
            if x % i == 0:
                x=x-i
                print(i)
            teller =1