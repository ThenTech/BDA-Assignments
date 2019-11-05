# write your code here
x = int(input())

sum = 0

for i in range(1, x+1):
    for j in range(1, i+1):
        sum += j
        
print(sum)
    