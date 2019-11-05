def is_magic_square(matrices):
    length_of_column = len(matrices[0])
    length_of_row = len(matrices)
    rowResults = [0]*length_of_column
    colResults = [0]*length_of_row
    for i in range(0, length_of_column):
        colSum = 0
        rowSum = 0
        for j in range(0, length_of_row):
            if j <= 0:
                break
            colSum += matrices[i][j]
            rowSum += matrices[j][i]
            rowResults[i] = rowSum
            colResults[i] = colSum


    rowElement = rowResults[0]
    colElement = colResults[0]
    for i in range(0, length_of_row):

        if rowElement != rowResults[i]:
            return False

    for i in range(0, length_of_column):
        if colElement != colResults[i]:
            return False

    return True