x = int(input())
tot = 0
d= 1
for i in range(1,x+1):
    d *= i
    tot += d
print(tot)