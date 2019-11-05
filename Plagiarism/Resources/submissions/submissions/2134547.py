a = int(input())
sum = 0

for x in range(1, a):
    for y in range(1, x):
        x *= y
    sum += x
    
print(sum)