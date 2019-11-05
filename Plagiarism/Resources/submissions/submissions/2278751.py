def is_prime(x):
    isPrime = True
    for i in range(2, x):
        isPrime = isPrime and x % i != 0
    return isPrime


def all_primes_upto(x):
    for i in range(2, x + 1):
        if (is_prime(x)):
            print(i)


def next_prime(x):
    while (not is_prime(x)):
        x = x + 1
    return x


def factorize(x):
    factor = 2
    while (x != 1):
        while (x % factor == 0):
            print(factor, end=" ")
            x = x // factor

        factor = next_prime(factor + 1)
    print()


examples = [126, 36, 1260, 3003]
for example in examples:
    factorize(example)
