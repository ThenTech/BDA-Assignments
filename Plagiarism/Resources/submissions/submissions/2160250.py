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
    i = 1
    while i <= x:
        k = 0
        if x % i == 0:
            j = 1
            while j <= i:
                if i % j == 0:
                    k += 1
                j += 1
            if k == 2:
                print(i)
        i += 1


print(factorize(126))
