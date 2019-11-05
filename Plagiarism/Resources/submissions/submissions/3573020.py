x_value = int(input("Give a number:"))
y_value = int(input("Give another number:"))

product_x = 1
product_y = 1
product_x_y = 1
minus_x_y = x_value - y_value

for i in range(x_value):
    product_x = product_x * (i + 1)

for j in range(y_value):
    product_y = product_y * (j + 1)

for k in range(minus_x_y):
    product_x_y = product_x_y * (k+1)

value = product_x / (product_y * product_x_y)
    

print(value)