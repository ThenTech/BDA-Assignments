x = int(input())
y = int(input())
for i in range(1,(x*y)+1):
    if i % y ==0:
        print(i)
    else:
        print(i,end=" ")
    