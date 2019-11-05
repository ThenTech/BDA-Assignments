# write your code here

x = int(input("Val for x:"))
sum_of_val = 0

for val in range(1, x+1):
    for y in range(1, val+1):
        sum_of_val += y
    
print(sum_of_val)