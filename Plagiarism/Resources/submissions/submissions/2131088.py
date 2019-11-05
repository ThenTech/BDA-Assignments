x = int(input())
y = int(input())

for i in range(1,y+1):
    for j in range(1,x+1):
        print(j+7*i, end=" ")
    print(" \n")
    