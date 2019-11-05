x = int(input(""))
y = int(input(""))

teller = 1
for i in range(y):
    for j in range(x):
        print(teller, end=" ")
        teller = teller + 1
    print()