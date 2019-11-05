def is_prime(x):
    if x % 2 != 0 and x % 3 != 0 and x > 0 and x != 1 and x % 5 != 0 and x % 7 != 0:
        return True
    elif x == 3 or x == 2 or x == 5 or x == 7:
        return True
    else:
        return False
print(is_prime(3))

def all_primes_upto(x):
    for i in range(x+1):
        if is_prime(i):
            print(i)
    return
print(all_primes_upto(13))

def factorize(x):
    for x in range(9999):
        if x // 2 = 0:
            x =  x / 2
            print(2)
        elif x // 3 = 0:
            x =  x / 3
            print(3)
        elif x // 5 = 0:
            x =  x / 5
            print(5)
        elif x // 7 = 0:
            x =  x / 7
            print(7)
        elif x // 11 = 0:
            x =  x / 11
            print(11)
        elif x // 13 = 0:
            x =  x / 13
            print(13)
        elif x // 17 = 0:
            x =  x / 17
            print(17)
        elif x // 19 = 0:
            x =  x / 19
            print(19)
        elif x // 23 = 0:
            x =  x / 23
            print(23)
        else:
        continue