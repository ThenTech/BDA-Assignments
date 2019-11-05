def is_magic_square(matrix):
    count = 0
    diagonaal = 0
    for i in range(len(matrix)):
        som = 0
        diagonaal += matrix[i][i]
        for j in range(len(matrix[i])):
            if matrix[i][j] not in alle:
                alle.append(matrix[i][j])
            else:
                return False
            kollom = 0
            count += 1
            som += matrix[i][j]
            for k in range(len(matrix)):
                kollom += matrix[k][j]
            if count == 1:
                m = kollom
            if kollom != m:
                return False
        if som != m:
            return False
    if diagonaal != m:
        return False
    return True