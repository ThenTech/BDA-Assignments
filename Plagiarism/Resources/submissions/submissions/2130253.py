# write your code here

val = int(input("Val for x:"))
pro_of_val = 0

for x in range(1, val+1):
    pro_of_val *= x
    
print(pro_of_val)