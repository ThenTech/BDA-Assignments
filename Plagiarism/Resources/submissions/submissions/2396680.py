def is_prime(x):
    if x < 2:
        return False
    isPrime = True
    for i in range(2, x):
        isPrime = isPrime and x % i != 0
    return isPrime


def all_primes_upto(x):
    for i in range(2, x + 1):
        if is_prime(i):
            print(i)


def next_prime(x):
    while not is_prime(x):
        x += 1
    return x


def factorize(x):
    factor = 2
    while x != 1:
        while x % factor == 0:
            print(factor)
            x //= factor

        factor = next_prime(factor + 1)


examples = [126, 36, 1260, 3003]
for example in examples:
    factorize(example)
