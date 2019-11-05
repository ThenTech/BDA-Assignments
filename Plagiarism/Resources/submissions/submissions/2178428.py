def is_prime(x):
    if x < 0:
        return False
    elif x == 3 or x == 2:
        return True
    elif x == 1:
        return False
    elif x < 10:
        if (x % 1 == 0) and (x % x == 0):
            if (x % 2 != 0) and (x % 3 != 0):
                return True
            else:
                return False
    else:
        if (x % 1 == 0) and (x % x == 0):
            if (x % 2 != 0) and (x % 3 != 0) and (x % 5 != 0) and (x % 7 != 0):
                return True
        else:
            return False


def all_primes_upto(x):
    for el in range(1,x+1):
        antw  = is_prime(el)
        if antw == True:
            print(el)