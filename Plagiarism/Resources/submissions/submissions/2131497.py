# write your code here
response = input("What is the n")
n = int(response)
product = 1
sum = 0

for i in range(1, n+1):
    product = product*i
    sum = sum + product
print(sum)