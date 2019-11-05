def is_prime(x):
    counter = 0
    for i in range(2,x+1):
        if x % i == 0:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def all_primes_upto(x):
    for i in range(1, x+1):
        if is_prime(i) == True:
            print(i)

def factorize(x):
    i = 2
    while i <= x:
        if is_prime(i) == True:
            if x % i == 0:
                x //= i
                print(i)
            else:
                i += 1
        else:
            i += 1