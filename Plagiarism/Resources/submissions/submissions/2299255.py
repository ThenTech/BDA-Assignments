def matrix1(mat):
    for i in range(0,2):
        for j in range(0, len(mat[0])):
            for q in range(0, 2):
                for z in range(0, len(mat[0])):
                    if mat[i][j] == mat[q][z] and i != q:
                        return False
    return True
sumtot = 0
def is_magic_square(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return True
    elif len(matrix) != len(matrix[0]):
        return False
    n = len(matrix[0])
    checkTrue = matrix1(matrix)
    if not checkTrue:
        return False
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum += matrix[i][j]
        if i == 0:
            sumtot = sum
        else:
            if sum != sumtot:
                return False
    

    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum += matrix[j][i]
        if i == 0:
           sumtot = sum
        else:
            if sum != sumtot:
                return False
    

    for j in range(0, n):
        sum = 0
        for i in range(0, n):
            sum += matrix[i][i]
        if sum != sumtot:
            return False
    sum = 0
    for i in range(0, n):

        for j in range(0, n):
            if i + j == 2:
                sum += matrix[i][j]
    if sum != sumtot:
        return False
    return True