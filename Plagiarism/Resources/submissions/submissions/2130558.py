# write your code here
x = int(input("Give x a value:"))
y = int(input("Give y a value:"))

for j in range(y):
    for i in range(x):
        print(i+1+j*x, end = " ")
    print()

