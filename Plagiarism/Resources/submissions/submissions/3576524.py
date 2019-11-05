# write your code here

x = int(input())
y = int(input())

product = 1
for i in range(1, y+1):
    product *= ((x-y+i)/i)

print(int(product))