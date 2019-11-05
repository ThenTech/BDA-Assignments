def is_magic_square(matrix):
    totsum = 0
    for i in matrix:
        for j in i:
            totsum += j
            break

    recent = []
    for i in matrix:
        if i not in recent:
            recent.append(i)
        else:
            return False

    for i in matrix:
        rowsum = 0
        for j in i:
            rowsum += j
        if rowsum != totsum:
            return False

    for i in range(len(matrix)):
        colsum = 0
        for j in range(len(matrix)):
            colsum += matrix[j][i]
        if colsum != totsum:
            return False

    diasum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                diasum += matrix[i][j]
    if diasum != totsum:
        return False

    return True
