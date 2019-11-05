def sum_first_row(matrix):
    sum = 0
    for i in range(len(matrix[0])):
        sum += matrix[0][i]
    return sum
    
    
def check_hor(matrix, sum):
    current_sum = 0
    for i in matrix:
        current_sum = 0
        for j in i:
            current_sum += j
        if sum != current_sum:
            break
    if sum != current_sum:
        return False
    return True

def check_hor(matrix, sum):
    current_sum = 0
    for i in matrix:
        current_sum = 0
        for j in i:
            current_sum += j
        if sum != current_sum:
            return False
    return True
    
def check_dia(matrix, sum):
    current_sum = 0
    for i in range(len(matrix)):
        current_sum += matrix[i][i]
    if sum != current_sum:
        return False
    current_sum = 0
    for i in range(len(matrix)):
        current_sum += matrix[i][len(matrix)-i-1]
    if sum != current_sum:
        return False
    return True
    
def check_ver(matrix, sum):
    current_sum = 0
    for i in range(len(matrix)):
        current_sum = 0
        for j in range(len(matrix)):
            current_sum += matrix[j][i]
        if sum != current_sum:
            return False
    return True


def is_unique(matrix):
    list = []
    for i in matrix:
        for j in i:
            if j in list:
                return False
            else:
                list.append(j)
    return True

def is_magic_square(matrix):
    sum = sum_first_row(matrix)
    if not is_unique(matrix):
        return False
    if not check_hor(matrix, sum):
        return False
    if not check_ver(matrix, sum):
        return False
    if not check_dia(matrix, sum):
        return False
    return True
