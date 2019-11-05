def is_prime(num):
    """Returns True if the given number is a prime number"""
    if num > 1:
        for x in range(2, num):
            if (num % x == 0):
                return False
        return True
    return False


def all_primes_upto(max_num):
    for i in range(2, max_num):
        if is_prime(i):
            print(i)
        
def factorize(number):
    i = 1
    while i < number:
        i += 1
        if number % i == 0:
            number /= i
            print(i)
            i = 1
