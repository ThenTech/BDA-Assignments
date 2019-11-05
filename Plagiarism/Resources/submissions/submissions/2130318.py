limit = int(input())

result = limit

for x in range(limit-1):
    result *= limit
    
print(result)