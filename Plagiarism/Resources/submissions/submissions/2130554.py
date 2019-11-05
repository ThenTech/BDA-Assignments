# write your code here

x = int(input("Input value x"))

output = 1

for i in range(x):
    output = output * (x-i)
    
print(output)