# write your code here

x = int(input("input x:"))

totalsum = 0

for i in range(x):
    i = i + 1
    sum = 0 
    for y in range(i):
        y = y + 1
        sum = sum + y
    totalsum = totalsum + sum
    
print(totalsum)