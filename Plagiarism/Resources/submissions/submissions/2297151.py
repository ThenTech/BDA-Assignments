def equal_row_sum(matrix):
    matrix_rows = len(matrix)
    sum_row = [1] * matrix_rows

    for row in range(matrix_rows):
        for element in matrix[row]:
            sum_row[row] += element
        if row > 0 and sum_row[row] != sum_row[row-1]:
            return False
    return True


def make_template_matrix(matrix):
    template_matrix = []
    elements = len(matrix)
    for row in matrix:
        template_matrix.append(["blank"] * elements)
    return template_matrix


def is_unique_matrix(matrix):
    unique_matrix = make_template_matrix(matrix)
    # nxn matrix
    n = len(matrix)

    for row in range(n):
        for index in range(n):
            # Checking equal elements in all rows
            for i in range(n):
                if matrix[index] in unique_matrix[i]:
                    return False

            # If element not in unique_matrix put element in unique_matrix
            unique_matrix[row][index] = matrix[row][index]
    return True


def is_nxn(matrix):
    matrix_rows = len(matrix)
    matrix_elements = 0
    for row in matrix:
        for element in row:
            matrix_elements += 1
    return matrix_rows == matrix_elements/matrix_rows


def is_even(matrix):
    return len(matrix) % 2 == 0


def is_magic_square(matrix):
    if is_even(matrix):
        print("even")
        return False

    if not is_nxn(matrix):
        print("not nxn")
        return False

    if not equal_row_sum(matrix):
        print("not equal sums")
        return False

    if not is_unique_matrix(matrix):
        print("not unique")
        return False
    return True