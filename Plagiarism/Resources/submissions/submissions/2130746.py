x = int(input("x = "))
y = int(input("y = "))
top = 1
bottom = 1
bottom_2 = 1

if x < 1 or y < 1:
    print("x and y have to be more than 0")
else:
    for value in range(1, x + 1):
        top = top * value
    for value in range(1, y + 1):
        bottom = bottom * value
    for value in range(1,x - y + 1):
        bottom_2 = bottom_2 * value

    coefficient = int(top / (bottom * bottom_2))

    print(coefficient)