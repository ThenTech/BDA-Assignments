# write your code here
response_x = input("What is x")
response_y = input("What is y")
x = int(response_x)
y = int(response_y)
product_x=x
product_y=y
product_result=1


for i in range(y):
    product_x = x
    product_y = y
    product_result = ((x-i)/(y-i))*product_result
print (int(product_result))