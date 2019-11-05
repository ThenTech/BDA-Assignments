x = int(input())
y = int(input())
z = x - y
b = 1
a = 1
c = 1

for i in range(x):
    a = a * x
    x = x - 1

for i in range(y):
    b = b * y
    y = y - 1

for i in range(z):
    c = c * z
    z = z - 1
d = a/(b * c)
    
print(int(d))