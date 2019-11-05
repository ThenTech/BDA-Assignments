x = int(input())
y = int(input())
tot = 0
for i in range(y):
    tot += ((x-i)/(y-i))
print(tot)