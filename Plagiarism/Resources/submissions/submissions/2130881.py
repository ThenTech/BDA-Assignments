x = input("X = ")
x = int(x)
y = input("Y = ")
y = int(y)
output = 1
for i in range(y):
    output *= (x-i)/(y-i)
print(output)