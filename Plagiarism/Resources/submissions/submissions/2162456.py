def is_prime(x):
    if x % 2 != 0 and x % 3 != 0 and x > 0 and x != 1 and x % 5 != 0 and x % 7 != 0:
        return True
    elif x == 3 or x == 2 or x == 5 or x == 7:
        return True
    else:
        return False
print(is_prime(3))

def all_primes_upto(x):
    for i in range(x+1):
        if is_prime(i):
            print(i)
    return
print(all_primes_upto(13))