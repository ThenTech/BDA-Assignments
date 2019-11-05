def is_magic_square(matrix):
    if len(matrix) % 3 == 0:
        sum_row_first = 0
        sum_row = 0
        row = 0
        index = 0

        unique_matrix = list(range(len(matrix)))
        for i in range(len(unique_matrix)):
            unique_matrix[i] = ["blank"] * 3

        for element in matrix[0]:
            sum_row_first += element

        for rows in matrix:
            for element in rows:
                sum_row += element

                if element in unique_matrix:
                    return False
                unique_matrix[row][index] = element
                index += 1

            if sum_row != sum_row_first:
                return False

            sum_row = 0
            index = 0
            row += 1
        return True
    return False
