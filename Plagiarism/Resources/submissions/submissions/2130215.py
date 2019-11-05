x = int(input("X: "))
y = int(input("Y: "))

result = 1
while (y > 0):
    result *= x/y
    x -= 1
    y -= 1

print(round(result))