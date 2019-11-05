a = int(input())
b = int(input())

f = 1
for i in range(1, b+1):
    for j in range(1, a+1):
        print(f, end=" ")
        f += 1
    print()