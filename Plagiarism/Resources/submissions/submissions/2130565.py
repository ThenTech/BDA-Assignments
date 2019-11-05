y = int(input("How many rows?: "))
x = int(input("How many Columns?: "))
z = 0
for i in range(x):
    for c in range(y):
        z += 1
        print(z, end=" ")
    print()# write your code here