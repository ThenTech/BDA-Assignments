x = int(input())

for i in (1, x+1):
    y = 0
    for j in (1, i+1):
        y += j
    z += y
print(z)