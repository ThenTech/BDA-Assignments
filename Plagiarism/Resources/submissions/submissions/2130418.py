x = float(input())
y = float(input())

total = 1.0;

for i in range(y):
    total*=(x-(i*y))/(y-i)

print(total)