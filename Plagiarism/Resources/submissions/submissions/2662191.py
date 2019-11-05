# write your code here
y = input("How many columns?")
x = input("How many rows?")

x = int(x)
y = int(y)

for i in range(0,x):
    for j in range(1,y+1):
        print(i * y + j, end=" ")
    print()