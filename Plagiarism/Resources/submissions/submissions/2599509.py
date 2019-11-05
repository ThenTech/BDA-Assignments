x = int(input("x"))
y = int(input("y"))
xx = 1
yy = 1
for i in range(y):
    xx *= (x-i)
    yy *= (y-i)
print(int(xx/yy))