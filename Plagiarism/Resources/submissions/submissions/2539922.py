x = int(input())
y = int(input())
prod = 1
for i in range(0, y):
    prod *= int((x - i)/(y - i))
print(prod)