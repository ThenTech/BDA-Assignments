x = int(input(" x: "))
resultado = 0
for i in range(1, x + 1):
    for j in range(1, i + 1):
        resultado = resultado + j
print( resultado)