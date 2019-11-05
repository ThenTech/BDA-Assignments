def is_unique(matrix):
    list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] in list):
                return False
            else:
                list.append(matrix[i][j])
    return True

def check_row(matrix):
    sumarray = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += matrix[i][j]
        sumarray.append(sum)
    for i in range(len(sumarray)-1):
        if (sumarray[i] != sumarray[i+1]):
            return False
    return True


def check_coll(matrix):
    sumarray = []
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        sumarray.append(sum)
    for i in range(len(sumarray) - 1):
        if (sumarray[i] != sumarray[i + 1]):
            return False
    return True

def check_diag(matrix):
    sumarray = []
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    sumarray.append(sum)
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][len(matrix)-1-i]
    sumarray.append(sum)
    for i in range(len(sumarray) - 1):
        if (sumarray[i] != sumarray[i + 1]):
            return False
    return True


def is_mag_square(matrix):
    if (is_unique(matrix) and check_row(matrix) and check_coll(matrix) and check_diag(matrix)):
        return True
    else:
        return False


