def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    else:
        return False


def all_primes_upto(x):
    new_string = ''
    d = 0
    for i in range(x+1):
        if is_prime(i):
            print(i)

def factorize(x):
    remain = x
    for i in range(x):
        if is_prime(i):
            for q in range(x):
                if remain % i == 0:
                    print(i)
                    remain /= i
