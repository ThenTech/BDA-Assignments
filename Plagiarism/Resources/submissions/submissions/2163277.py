def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True


def all_primes_upto(x):
    for i in range(x + 1):
        check = True
        if i == 0:
            continue
        elif i == 2:
            print(i)
            continue
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                check = False
                break
        if check:
            print(i)


def factorize(x):
    i = 2
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            print(i)
    if x > 1:
        print(x)