def is_prime(x):
    # declerations

    #function looks for prime
    if x > 1:
        for i in range(x-1):
            if x % (i+1) == 0 and i+1 != 1 and i+1 != x:
                return False
        return True
    else:
        return False

def all_primes_upto(x):
    for i in range(x):
        if is_prime(i) == True:
            print(i)

def factorize(x):
    i = 0

    while i <= x:
        if is_prime(i) == True:

            if x/i % int(x/i) == 0:
                print(i)
                x = x/i
                i = 0
            else:
                i += 1
        else:
            i += 1