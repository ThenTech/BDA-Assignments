def lijstomzetter(matrix):
    vector = matrix[0]
    for i in range(1, len(matrix)):
        vector = vector + matrix[i]
    return vector

def kolom(matrix):
    m = sum(matrix[0])
    for j in range(len(matrix)):
        x = matrix[0][j]
        for i in range(1,len(matrix)):
            x = x + matrix[i][j]
        if x != m:
            return False
        else:
            return True

def diagonaal(matrix):
    m = sum(matrix[0])
    x = matrix[0][0]
    for i in range(1,len(matrix)):
        x = x + matrix[i][i]
    if x != m:
        return False
    else:
        return True

def uniciteit(matrix):
    vectorlijst = lijstomzetter(matrix)
    for i in range(len(vectorlijst)):
        count = 0
        x = vectorlijst[i]
        for j in range(len(vectorlijst)):
            if vectorlijst[j] == x:
                count = count + 1
            if count == 2:
                return False
    return True

def som(matrix):
    m = sum(matrix[0])
    for i in range(len(matrix)):
        if sum(matrix[i]) != m:
            return False
    if not kolom(matrix):
        return False
    if not diagonaal(matrix):
        return False
    return True

def is_magic_square(matrix):
    if uniciteit(matrix) and som(matrix):
        return True
    else:
        return False