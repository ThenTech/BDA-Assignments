# write your code here

x = int(input("x value:"))
y = int(input("y value:"))

for y_val in range(1, y + 1):
  for x_val in range(1, x + 1):
    print(x_val * y_val, end=" ")
  print()