def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


def all_primes_upto(x):
    for i in range(2, x + 1):
        if is_prime(i):
            print(i)


def priemlijst(x):
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
    
def factorize(x):
    prime_list = priemlijst(x)
    while x > 1:
        i = 0
        while True:
            if x % primelist[i] == 0:
                print(i)
                break
            i += 1
        x /= primelist[i]
        