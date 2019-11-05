def is_prime(x):
    prime = True
    if x == 0 or x == 1 or x < 0:
        prime = False
    else:
        for i in range(2,x):
            if x % i == 0:
                prime = False
    return prime


def all_primes_upto(x):
    for i in range(x+1):
        if is_prime(i):
            print(i)

def factorize(x):
    getal = x
    for i in range(x):
        while is_prime(i) and getal % i == 0:
            getal = getal/i
            print(i)
        if getal == 1:
            return