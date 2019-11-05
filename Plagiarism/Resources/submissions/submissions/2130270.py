x = int(input())
y = int(input())

for a in range(y):
    for b in range(x):
        print(y*(b//x)+b+1, end=" ")
    print()
