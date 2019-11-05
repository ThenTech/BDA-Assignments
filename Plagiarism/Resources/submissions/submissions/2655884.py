def is_magic_square(ls):
    tot_sum = 0
    # checking rows
    for row in ls:
        row_sum = 0
        for ele in row:
            row_sum += ele
        if tot_sum == 0:
            tot_sum = row_sum
        else:
            if tot_sum != row_sum:
                return False
    # checking cols
    for counter in range(len(ls)):
        col_sum = 0
        for row in ls:
            col_sum += row[counter]
        if col_sum != tot_sum:
            return False
    # check left_diagonal
    left_dia_sum = 0
    for index in range(len(ls)):
        left_dia_sum += ls[index][index]
    if left_dia_sum != tot_sum:
        return False

    # check right_diagonal
    right_dia_sum = 0
    index = len(ls) - 1
    row_index = 0
    while index >= 0:
        right_dia_sum += ls[row_index][index]
        index -= 1
        row_index += 1
    if right_dia_sum != tot_sum:
        return False

    return True