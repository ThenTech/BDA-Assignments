x = int(input())
y = int(input())

for i in range(y):
    for j in range(1,x+1):
        print(j+x*i, end=" ")
    print("\n")
    