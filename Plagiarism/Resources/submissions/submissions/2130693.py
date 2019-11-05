x = int(input("x = "))
y = int(input("y = "))

if x < 1 or y < 1:
    print("x and y have to be more than 0")
else:
    coefficient = int((x/y) * ((x-1)/(y-1)) * ((x-y+1)/1))

    print(coefficient)