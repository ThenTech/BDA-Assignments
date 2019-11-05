x = int(input(''))
som = 0

def fac_rec(n):
    if n == 0:
        return 1
    else:
        return n*fac_rec(n - 1)
        

for i in range(1, x + 1):
    som += fac_rec(i)

print(som)
    
