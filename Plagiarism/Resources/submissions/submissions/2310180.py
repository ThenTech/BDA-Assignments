x = int(input())

y = 0
for i in range(1, x+1):
    z = 0
    for j in range(1, i+1):
        z = j
        y += z
print(y)