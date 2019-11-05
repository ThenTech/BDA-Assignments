x = int(input())
y = 0
z = 0
a = 0

for j in range(x):
    y = 0
    for i in range(x-z):
        y = y + (i+1)
    z = z + 1
    a = a + y
print(a)