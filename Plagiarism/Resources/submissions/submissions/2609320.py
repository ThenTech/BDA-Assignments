def is_prime(x):
    if x < 2:
        return False
    for i in range(2,x-1):
        if x % i == 0:
            print("False")
            return
    print("True")


def all_primes_upto(x):
    notPrime = False
    if x < 2:
        return
    for i in range(2,x+1):
        for j in range(2, i):
            if i % j == 0:
                notPrime = True
                break
        if notPrime == False:
            print(i)
        else:
            notPrime = False


def factorize(x):
    d = 2
    while d*d <= x:
        while (x % d) == 0:
            print(d)
            x //= d
        d += 1
    if x > 1:
       print(x)
    return
