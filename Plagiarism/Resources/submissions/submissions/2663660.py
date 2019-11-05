def get_sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def is_odd_matrix(matrix):
    rows = len(matrix)
    if rows % 2 != 1:
        return False
    for row in matrix:
        columns = len(row)
        if columns != rows:
            return False
    return True


def is_magic_square(matrix):
    sum = get_sum(matrix[0])
    unique_list = []
    good_shape = is_odd_matrix(matrix)
    if not good_shape:
        return False

    for row in matrix:
        row_sum = 0
        for num in row:
            if num not in unique_list:
                unique_list.append(num)
                row_sum += num
            else:
                return False
        if row_sum != sum:
            return False
    return True