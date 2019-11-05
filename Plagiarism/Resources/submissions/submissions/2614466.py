def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            return False
    return True


def all_primes_upto(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i)


def factorize(n):
    priem = []
    lel = []
    for i in range(2, n+1):
        if is_prime(i):
            priem.append(i)
    priem.reverse()
    for i in priem:
        while n % i == 0:
            lel.append(i)
            n = n//i
    lel.reverse()
    for i in lel:
        print(i)
