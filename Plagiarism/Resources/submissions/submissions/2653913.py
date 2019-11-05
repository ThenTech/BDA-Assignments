x = int(input())
y = int(input())
zz = 1
for i in range(y):
    z = (x - i) / (y - i)
    zz = zz * z
print(int(zz)