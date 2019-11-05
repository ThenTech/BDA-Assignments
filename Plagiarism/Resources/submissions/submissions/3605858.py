def is_magic_square(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        total_sum += matrix[i][0]

    li = []
    for row in matrix:
        counter_col = 0

        for col in row:
            counter_col += 1
            if col not in li:
                li.append(col)
            else:
                return False
        if (counter_col != len(matrix)):
            return False

    diag_sum = 0
    for row in range(len(matrix)):
        col_sum = 0
        row_sum = 0
        for col in range(len(matrix[row])):
            col_sum += matrix[row][col]
            row_sum += matrix[col][row] # omgewisseld
            if(row == col):
                diag_sum += matrix[row][col]

        if(col_sum != total_sum != row_sum):
            return False
    if(diag_sum != total_sum):
        return False
    else:
        return True