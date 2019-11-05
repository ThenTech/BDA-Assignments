limit = int(input())

result = limit

for x in range(limit):
    result *= (x+1)
    
print(result)