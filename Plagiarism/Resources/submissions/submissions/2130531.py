# write your code here

x = int(input("Val for x:"))
sum_of_val = 0

for val in range(x):
    for y in range(val):
        sum_of_val += val
        print(sum_of_val)
    
