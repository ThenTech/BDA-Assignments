def is_prime(x):
    if x<10:
        for i in [2, 3, 5, 7]:
            if i==x:
                return True
        else:
            return False
    if x>10:
        for i in [2,3,5,7]:
            if x%i==0:
                return False
        else:
            return True

def all_primes_upto(x):
    for i in range(x):
        if is_prime(i) == True:
            print(i)
    return ""
def factorize(x):
    for i in range(1,x):
        if is_prime(i)==True:
            while x%i==0:
                x=x/i
                print(i)
    return""
