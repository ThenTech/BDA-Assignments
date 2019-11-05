def is_prime(x):
    test = True
    if x < 1 or x == 1:
        test = False
    for j in range(2, x):
        if x%j == 0:
            test = False

    print(test)

def all_primes_upto(x):
    pass


def factorize(x):
    pass