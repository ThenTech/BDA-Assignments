def is_prime(x):
    if x < 2:
        print(False)

    elif x == 2:
        print(True)

    else:
        for z in range(x-1):
            if x % (z+2) == 0 and x != z+2:
                print(False)
                break
            elif x % (z+2) == 0 and x == z+2:
                print(True)


def all_primes_upto(x):
    pass


def factorize(x):
    pass