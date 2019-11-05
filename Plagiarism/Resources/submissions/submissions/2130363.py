x = int(input())
y = int(input())

result = 1
for i in range(y):
    result *= (x-i)/(y-i)
    
print(result)