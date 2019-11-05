numbery = int(input("Give me a value for x: "))
numberx = int(input("Give me a value for y: "))
for x in range(numberx):
    for y in range(1, numbery + 1):
        print(x*numbery+y, end=" ")
    print()
