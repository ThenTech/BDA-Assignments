x = int(input("Give a value for x:"))
y = int(input("Give a value for y:"))

for i in range(0, y):
    for j in range(1, x+1):
        print(i*x+j, end = " ")
    print()