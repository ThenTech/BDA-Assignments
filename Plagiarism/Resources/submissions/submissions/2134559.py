a = int(input())
sum = 0

for x in range(1, a+1):
    for y in range(1, x+1):
        sum += y
        
print(sum)