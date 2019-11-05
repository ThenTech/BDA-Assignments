limit = int(input())

result = limit

for x in range(limit):
    result *= limit
    
print(result)