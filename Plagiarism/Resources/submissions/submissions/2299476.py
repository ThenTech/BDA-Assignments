def is_unique(l):
    newlist = []
    for p in l:
        newlist += p
    for i in range(len(newlist)):
        for j in range(1, len(newlist)-i):
            if newlist[i] == newlist[i+j]:
                return False
    return True

def is_magic_square(matrix):
    som = 0
    if is_unique(matrix) == False:
        return False
    #kolommen
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            som += matrix[j][i]
        if i != 0 and som != storage:
            return False
        storage = som
        som = 0
    #rijen
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            som += matrix[i][j]
        if som != storage:
            return False
        storage = som
        som = 0
    #diagonalen
    for i in range(len(matrix)):
        som += matrix[i][i]
    if som != storage:
        return False
    return True
    