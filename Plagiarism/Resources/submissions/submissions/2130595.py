# write your code here
response_x = input("What is x")
response_y = input("What is y")
x = int(response_x)
y = int(response_y)

product = 1
for i in range(y):
    for j in range(i*x+1, (i+1)*x+1):
        print(j, end=" ")
    print()