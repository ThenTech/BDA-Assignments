# write your code here
x = int(input())
y = int(input())

for i in range(1, x*y+1):
    print(i, end=" ")
    for j in range(x):
        print()