def checkRowsAndColumn(matrix, m):
    rowCount = 0
    columnCount = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            rowCount += matrix[i][j]
            columnCount += matrix[j][i]
        if m != rowCount or m != columnCount:
            return False
        else:
            rowCount = 0
            columnCount = 0
    return True
    
    
def isUnique(matrix):
    uniqueMatrix = []

    for i in range(len(matrix)):
        for j in range(len(matrix)): 
            if matrix[i][j] in uniqueMatrix:
                return False
            else:
                uniqueMatrix.append(matrix[i][j])
    return True

def is_magic_square(matrix):
    if len(matrix) != len(matrix[len(matrix)-1]):
        return False
    m = 0
    diagonalCount = 0
    for i in range(len(matrix)):
        diagonalCount += matrix[i][i]
        m += matrix[0][i]
    
    if isUnique(matrix) and checkRowsAndColumn(matrix, m) and m == diagonalCount:
        return True
    else: 
        return False