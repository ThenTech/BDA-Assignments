def is_magic_square(matrix):
    tot = 0
    som = 0
    for i in range(len(matrix)):
       tot += som 
       som = 0
       for j in range(len(matrix)):
           som += matrix[i][j]
    if tot / i != som:
       return False
    tot = 0
    x = som
    som = 0
    for i in range(len(matrix)):
        tot += som
        som = 0
        for j in range(len(matrix)):
            som += matrix[j][i]
    if tot / i != som or som != x:
        return False
    x = som
    som = 0
    for i in range(len(matrix)):
        som += matrix[i][i]
    if x != som:
        return False
    som = 0
    for i in range(len(matrix)):
        som += matrix[len(matrix)-i-1][len(matrix)-i-1]
    if x != som:
        return False
    return True
    