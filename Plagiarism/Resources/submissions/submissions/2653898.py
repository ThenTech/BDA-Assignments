x = int(input())
y = int(input())
zz = 1
for i in range(x+1):
    z = (x - i) / (y - i)
    zz = zz * z
print(zz)
    