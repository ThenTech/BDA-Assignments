def is_magic_square(matrix):
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
    
    value1 = True
    for i in list_sums:
        if i != sum_elements:
            value1 = False
            
    return value1