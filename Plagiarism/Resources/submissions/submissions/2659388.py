def check_row(matrix):
    tot_sum = 0
    for i in range(len(matrix)):
        tot_sum += rijsom(matrix[i])
    for i in range(len(matrix)):
        if rijsom(matrix[i]) != tot_sum / len(matrix):
            return False
    return True

def kolsom(matrix, rij):
    som = 0
    for i in range(len(matrix)):
        som += matrix[i][j]
    return som
    

def check_column(matrix):
    tot_sum = 0
    for j in range(len(matrix[i])):
        tot_sum += kolsom(matrix, j)
    for j in range(len(matrix[0])):
        if kolsom(matrix, j) != tot_sum / len(matrix):
            return False
    return True


def is_magic_square(matrix):
    if uniek(matrix):
        if check_row(matrix) and check_column(matrix):
            return True
        else:
            return False
    else:
        return False