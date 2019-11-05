x = int(input())
a = 1
b = 0
y = x
z = x
c = 0

for j in range(x):
    a = 1
    y = z - c
    
    for i in range(y):
        a = a * y
        y = y - 1
    
    c = c + 1
    b = b + a
    x = x - 1
print(b)