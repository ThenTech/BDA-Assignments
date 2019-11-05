def is_prime(x):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def all_primes_upto(x):
    for i in range(x):
        if is_prime(i):
            print(i)


def primes_upto(x):
    list = []
    for i in range(x):
        if is_prime(i):
            list.append(i)
    return list

def do_loop(x2, list2):
    i = 0
    for num in range(i, list2.__len__()):
        if x2 % list2[num] == 0:
            print(list2[num])
            x2 = int(x2 / list2[num])
            if x2 == 1:
                exit()
            do_loop(x2, list2)


def factorize(x):
    list = primes_upto(x)
    do_loop(x, list)