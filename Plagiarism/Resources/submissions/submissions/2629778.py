def is_prime(x):
    if x <= 1:
        return False
    if x ==2:
        return True
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
    return True


def all_primes_upto(x):
    for i in range(x):
        if is_prime(i) == True:
            print(i)
            

def factorize(x):
    nummer = 2
    q= True
    while q == True:
        nummer = function(nummer ,x)
        for i in string:
            c = True
            while c ==True:
                if x%int(i) ==0:
                    x = x/int(i)
                    print(i)
                if int(x)/int(i) ==1:
                    return
                c =False
            q = False

               
               
def function(nummer, x):
    for i in range(nummer,x):
        if is_prime(i) == True:
            return i
