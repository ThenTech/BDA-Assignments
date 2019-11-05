x = int(input())
y = 1
z = 0
for i in range(1, x+1):
    y = 1
    for j in range(1, i+1):
        y = j * y
    z += y
    
    
print(z)