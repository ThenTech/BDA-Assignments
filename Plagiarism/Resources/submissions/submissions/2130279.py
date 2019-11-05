x = int(input())
y = int(input())

for a in range(y):
    for b in range(x):
        print(a*((b+y*a)//x)+1, end=" ")
    print()
