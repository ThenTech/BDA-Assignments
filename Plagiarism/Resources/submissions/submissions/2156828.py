def is_prime(x):
    if x == 0 or x == 1: return False
    for i in range(2, x):
        if (x/i)%1 == 0: return False
    return  True

def all_primes_upto(x):
    for i in range(2, x):
        if is_prime(i): print(i)

def factorize(x):
    result = x
    i = 2
    while result>1:

        if is_prime(i):
            is_factor = result%i==0
            if is_factor:
                print(i)
                result = result/i

            else:
                i += 1
        else:
            i += 1