def is_magic_square(matrix):
    for i in range (0, len(matrix[1])):
        m2 = 0
        m3 = 0
        m4 = 0
        m5 = 0
        for j in range (0, len(matrix[1])):
            m2 += matrix [i][j]
            m3 += matrix [j][j]
            m4 += matrix [j][i]
            m5 += matrix [len(matrix[1])-1-j][len(matrix[1])-1-j]
        if m2 != m3:
            return False
        if i == len(matrix[1])-1:
            return True