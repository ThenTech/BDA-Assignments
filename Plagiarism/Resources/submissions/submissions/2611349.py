def is_prime(x):
    prime_counter = 0
    if not(x > 1):
        return False
    for i in range(2, 10):
        if x % i == 0:
            if x == i:
                prime_counter -= 1
            prime_counter += 1
    if prime_counter == 0:
        return True
    else:
        return False


def all_primes_upto(y):
    for i in range(2, y+1):
        if is_prime(i):
            print(i)


def factorize(z):
    result = z
    while True:
        if result == 1:
            return
        if is_prime(result):
            return
        else:
            for i in range(2, result):
                if is_prime(i) and (result % i) == 0:
                    print(i)
                    result //= i
                    if int(result) == int(i):
                        return
                    break



factorize(126)
is_prime(22)
all_primes_upto(25)