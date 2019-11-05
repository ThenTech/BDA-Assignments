# write your code here

x = int(input("x value:"))
y = int(input("y value:"))
curr_val = 0

for y_val in range(y):
    for x_val in range(x):
        curr_val += 1
        print(curr_val, end=" ")
    print()