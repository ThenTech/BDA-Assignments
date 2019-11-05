def unique_test(matrix):
    test_list = []
    for colum in matrix:
        for n in colum:
            test_list.append(n)
    for q in range(len(test_list)):
        if test_list[q] in test_list[q+1:]:
            return False
    return True


def is_magic_square(matrix):
    if not unique_test(matrix):
        return False
    columsum = 0
    colum_list = []
    for row in matrix:
        for i in row:
            columsum += i
        colum_list.append(columsum)
        columsum = 0
    for q in range(len(colum_list)-1):
        if colum_list[q] != colum_list[q+1]:
            return False

    rowsum = 0
    row_list = []
    for colum in range(len(matrix[0])):
        for i in range(len(matrix)):
            rowsum += matrix[i][colum]
        row_list.append(rowsum)
        rowsum = 0
    for q in range(len(row_list)-1):
        if row_list[q] != row_list[q+1]:
            return False
    return True