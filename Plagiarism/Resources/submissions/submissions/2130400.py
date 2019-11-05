x = int(input())
y = int(input())

total = 1;

for i in range(y):
    total*=int((x-(1*y))/(y-i))

print(total)