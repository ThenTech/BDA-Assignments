def is_prime(x):
    for i in range(2, 10):
        if x != i and x % i == 0 or x <= 1:
            return False
    return True

def all_primes_upto(x, y=0):
    list_of_primes = []
    for i in range(0, x):
        if is_prime(i):
            list_of_primes.append(i)
            if y == 0:
                print(i)
    return list_of_primes

def factorize(x):
    list_of_primes = all_primes_upto(x, 1)
    i = 0
    while x > 1:
        while x % list_of_primes[i] == 0:
            print(list_of_primes[i])
            x /= list_of_primes[i]
        i += 1