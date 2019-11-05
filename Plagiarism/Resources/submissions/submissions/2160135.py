def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False


def all_primes_upto(x):
    for num in range(x):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


def factorize(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
