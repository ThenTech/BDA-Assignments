a = int(input())
sum = 0

for x in range(a):
    for y in range(x):
        sum += y
        
print(sum)