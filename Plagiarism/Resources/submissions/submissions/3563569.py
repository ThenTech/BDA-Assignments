def is_magic_square(matrix):

    sum1 = 0
    sum2 = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum1 += matrix[i][j]

    

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i + 1 == -(j-len(matrix)):                        
                sum2 += matrix[i][j-len(matrix)]
    

    return bool(sum1 == sum2)