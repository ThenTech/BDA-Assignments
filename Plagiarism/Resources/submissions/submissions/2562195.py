def is_prime(x):
    prime = True
    if x > 1:
        for i in range (2, x):
            if x % i == 0:
                  return False
        return True
    else:
        return False

def all_primes_upto(x):
    for i in range(2, x+1):
        if is_prime(i):
            print(i)

def factorize(x):
    def prime_and_div(x, i):
        if is_prime(i) and (x % i == 0):
            x /= i
            print(i)
            prime_and_div(x, i)
    for i in range(x):
        prime_and_div(x, i)