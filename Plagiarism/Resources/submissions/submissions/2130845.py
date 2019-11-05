numberX = int(input())
numberY = int(input())

prodX = 1
for i in range(1, numberX+1):
    prodX *= i

prodY = 1
for i in range(1, numberY+1):
    prodY *= i

verschil = numberX-numberY
prodVerschil = 1
for i in range(1, verschil+1):
    prodVerschil *= i

result = int(prodX/(prodY*prodVerschil))
print(result)
