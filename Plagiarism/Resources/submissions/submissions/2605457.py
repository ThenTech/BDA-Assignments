def is_magic_square(matrix):

    value1 = True

    matrix_not_nested = []
    count_row = 0
    for row in matrix:
        count_row +=1
        count_element = 0
        for element in row:
            count_element += 1
            matrix_not_nested.append(element)
            
    for element in range(len(matrix_not_nested)):
        for element2 in range(len(matrix_not_nested)):
            if element2 != element:
                if matrix_not_nested[element] == matrix_not_nested[element2]:
                    value1 = False
                    break
        
        
    if count_row != count_element:
        value1 = False

    list_sums =[]
    for row in matrix:
        sum_elements = 0
        for element in row:
            sum_elements += element
        list_sums.append(sum_elements)

    for row in range(len(matrix)):  # need to get to columns
        sum_elements = 0
        for element in range(len(matrix)):
            sum_elements += matrix[element][row]
        list_sums.append(sum_elements)

    sum_elements = 0
    for row in range(len(matrix)):  # need to get to columns
        sum_elements += matrix[row][row]
    list_sums.append(sum_elements)

    sum_elements = 0
    for row in range(len(matrix)):  # need to get to columns
        sum_elements += matrix[row][row]
    list_sums.append(sum_elements)

    for i in list_sums:
        if i != sum_elements:
            value1 = False

    return value1