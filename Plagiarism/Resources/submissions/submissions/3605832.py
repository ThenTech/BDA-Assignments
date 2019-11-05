def is_magic_square(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        total_sum += matrix[0][i]

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