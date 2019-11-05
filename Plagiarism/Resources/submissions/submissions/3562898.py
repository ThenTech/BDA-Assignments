x = int(input("give an x: "))
y = int(input("give a y: "))

for i in range(y):
    for j in range(x):
        print((j+1) + x*i, end=" ")

    print(" ")