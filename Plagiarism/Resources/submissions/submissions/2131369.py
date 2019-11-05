x = input("input1 = ")
y = input("input2 = ")
n = 1
for i in range(0, int(y)):
    for j in range(1, int(x)+1):
        print(n, end=" ")  
        n = n + 1
    print()