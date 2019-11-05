x = int(input())
y = int(input())

for i in range(y):
    for j in range(x):
        print(j + (x * i), end = " ")
    print()
