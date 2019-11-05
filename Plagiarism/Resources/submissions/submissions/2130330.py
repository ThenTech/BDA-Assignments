x = int(input())
y = int(input())

for Y in range(0,y-1):
    for X in range(1,x):
        print((Y*X+X, end=" ")
    print(x+Y*x)

for X in range(1,x):
    print(X+(y-1)*X, end=" ")
print(x+(y-1)*x, end="")