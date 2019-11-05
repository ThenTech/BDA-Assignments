def is_prime(x):
    if x <= 1:
        return False
    if x ==2:
         return True
    if x%2 == 0:
         return False
    return True


def all_primes_upto(x):
    lijst = []
    for i in range(x):
        if is_prime(i) == True:
            lijst += str(i)
    return lijst

def factorize(x):
    string = all_primes_upto(x)
    for i in string:
       c = True
       while c ==True:
          if x%int(i) ==0:
               x = x/int(i)
               print(i)
          if int(x)/int(i) ==1:
               return
          c =False