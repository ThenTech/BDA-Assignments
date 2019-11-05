M = []
filas = int(input("filas: "))
columnas = filas

for t in range(filas):
    a = [0]* columnas
    M.append(a)


# Matrix coefficients

for i in range(filas):
    for j in range(columnas):
        M[i][j] = int(input("coefficient: ({0}{1})".format(i, j)))
print(M)

def suma_fila(M):
    nueva = []
    for i in range(filas):
        sumafilas = 0
        for j in range(columnas):
            sumafilas += M[i][j]

        nueva.append(sumafilas)
    return nueva


def suma_columnas(M):
    nuevacol = []
    for x in range(columnas):
        sumacolumnas = 0
        for y in range(filas):
            sumacolumnas += M[y][x] #OJO AQUI!!!
        nuevacol.append(sumacolumnas)
    return nuevacol


def traza(M):
    suma = 0
    for i in range(filas):

        suma += M[i][i]
    return suma



def magica(M):
    vecfilas = suma_fila(M)
    vectcolumnas = suma_columnas(M)
    for i in vecfilas:
        for j in vectcolumnas:
            if i == j == traza(M):
                return True
            else:
                return False