x = int(input(""))
y = int(input(""))
xFac = 1
yFac = 1
dFac = 1

for i in range(1, x + 1):
    xFac *= i

for i in range(1, y + 1):
    yFac *= i

for i in range(1, x-y+1):
    dFac *= i

result = xFac / (yFac * dFac)

print(int(result))