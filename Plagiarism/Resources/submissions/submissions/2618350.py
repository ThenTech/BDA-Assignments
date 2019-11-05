def is_matrix(matrix):
    being_matrix = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if len(matrix[i]) != len(matrix[j]) and i != j:
                being_matrix = False
        if len(matrix) != len(matrix[i]):
            being_matrix = False
    return being_matrix

def horizontal_sum(matrix):
    being_horizontal = True
    list_sums = []
    for element in range(len(matrix)):
        total = 0
        for number in matrix[element]:
            total += number
        list_sums.append(total)

    for i in list_sums:
        for j in list_sums:
            if i != j:
                being_horizontal = False

    return being_horizontal


def vertical_sum(matrix):
    being_vertical = True
    list_sums = []
    for element in range(len(matrix)):
        total = 0
        for element_double in range(len(matrix)):
            total += matrix[element_double][element]
        list_sums.append(total)

    for i in list_sums:
        for j in list_sums:
            if i != j:
                being_vertical = False
    return being_vertical


def diagonal_sum(matrix):
    being_diagonal = True
    list_sums = []
    total = 0
    total2 = 0
    for element in range(len(matrix)):
        total += matrix[element][element]
    for element in range(len(matrix)-1,-1, -1):
        total2+=matrix[element][element]

    return total == total2


def is_magic_square(matrix):
    being_matrix = is_matrix(matrix)  # call function
    if being_matrix == True:
        a = horizontal_sum(matrix)
        b = vertical_sum(matrix)
        c = diagonal_sum(matrix)
        return a == b and b == c
    else:
        return False