x = int(input("give the first number"))
y = int(input("give the second number"))



for i in range(x * y):
    print(i+1, end=" ")
    for k in range(x):
        if (i+1) == ((k+1) * y):
            print("")
    