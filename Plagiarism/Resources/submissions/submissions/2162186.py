def is_prime(x):
    for i in range(1000):
        if i == 1 or i == x or i == 0:
            i += 1
        else:
            return x % i == 0
    pass


is_prime(1)



def all_primes_upto(x):
    pass


def factorize(x):
    pass