x_value = int(input("Give a value for x: "))
y_value = int(input("Give a value for y:"))

for i in range(0, y_value):
    for j in range(1, x_value + 1):
        print(i * x_value + j, end=" ")
    print()
# write your code here