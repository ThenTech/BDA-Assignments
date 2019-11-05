x = int(input())
y = int(input())

result = 1
for i in range(y-1):
    result *= (x-i)/(y-i)