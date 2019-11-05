# write your code here

x = int(input("x"))
y = int(input("y"))

teller = 1
noemer = 1

for i in range(y):
    teller = teller * (x-i)
    noemer = noemer * (y-i)
    
print(teller//noemer)
