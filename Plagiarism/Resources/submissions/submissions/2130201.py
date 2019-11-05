x = int(input("number?"))
y = int(input("number?"))
k = 0
for i in range(y):
    for j in range(x):
        k += 1
        print(k,end=" ")
    print()