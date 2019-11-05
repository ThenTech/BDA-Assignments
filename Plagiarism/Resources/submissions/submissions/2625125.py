x = int(input())
y = int(input())
tot = 1
for i in range(y):
    tot *= ((x-i)/(y-i))
print(int(tot))