def is_prime(x):
    test = True
    if x < 1 or x == 1:
        test = False
    for j in range(2, x):
        if x%j == 0:
            test = False

    return test

def all_primes_upto(x):
    for q in range(2, x):
        check = is_prime(q)
        if check:
            print(q)
        else:
            pass



def factorize(x):
    pass