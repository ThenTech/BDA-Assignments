x = 0

def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False

result = is_prime(x)
print(result)



x = 0

def all_primes_upto(x):
    for j in range(2, x):
        if j == is_prime(x):
            print(j)


all_primes_upto(x)

def factorize(x):
    pass