def is_magic_square(matrix):
    if len(matrix) % 2 == 0 and len(matrix) == len(matrix[0]):
        if is_unique(matrix) == True:
            for i in matrix:
                if sum(matrix[i]) == sum(matrix[0]):
                    for j in i:
                        if sum(j) == sum(matrix[0]):
                            continue
                        else:
                            return False
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
    
def is_unique(l):
    teller1 = 0
    for i in l:
        teller2 = 0
        for j in l:
            if teller1 != teller2 and i == j:
                return False
            else:
                teller2 += 1
        teller1 += 1
    return True