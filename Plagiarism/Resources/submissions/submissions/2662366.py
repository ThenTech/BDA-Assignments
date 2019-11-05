def is_magic_square(matrix):
    row_lenght = len(matrix)
    column_lenght = len(matrix[0])
    #nxn?
    if row_lenght != column_lenght:
        return False

    # make 1 lenght matrix
    matrix2 = []
    for i in matrix:
        for j in i:
            matrix2.append(j)

    # getal uniek?
    for i in range(len(matrix2)-1):
        if matrix2[i] in matrix2[i+1:]:
            return False
            
    #m =?
    m = 0
    for i in range(len(matrix)):
        m += matrix[0][i]
    
    # som rij = 15?
    for i in matrix:
        sum_row = 0
        for j in i:
            sum_row += j
        if sum_row != m:
            return False
    sum_diag1 = 0
    sum_diag2 = 0
    # som kolom        
    for row in range(len(matrix)):
        sum_column = 0
        for column in range(len(matrix[row])):
            sum_column += matrix[column][row]
            if row == column: 
                sum_diag1 += matrix[row][column]
            if row + column == len(matrix)-1:
                sum_diag2 += matrix[row][column]
        if sum_column != m:
            return False
            
    if sum_diag1 != m or sum_diag2 != m:
            return False
    return True
