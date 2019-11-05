def is_magic_square(m):
    if is_square_matrix(m) and is_unique(m) and magic_sum(m):
        return True
    return False


def flatten(array):
    "Returns a 1D array from a 2D array"
    new_list = []
    for i in array:
        for j in i:
            new_list.append(j)
    return new_list

def is_unique(matrix):
    "Checks if al the elements in the list are unique, u need to flatten the 2D array"
    matrix = flatten(matrix)

    element_count = 0
    for element1 in matrix:
        for element2 in matrix:
            if element1 == element2:
                element_count += 1
        if element_count != 1:
            return False
        element_count = 0
    return True


def magic_sum(matrix):
    "Checks is the vertical and diagonal sum are equal"
    sum_list = []
    current_sum = 0
    
    # Vertical sum
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            current_sum += matrix[j][i]
        sum_list.append(current_sum)
        current_sum = 0

    # Diagonal sum
    for i in range(len(matrix)):
        current_sum += matrix[i][i]
    sum_list.append(current_sum)
    
    print(sum_list)

    # Checking al the sums
    for i in range(len(sum_list)):
        if sum_list[0] != sum_list[i]:
            return False
    return True



def is_square_matrix(matrix):
    "Checks if the given matrix is a square (nxn)"
    is_sq_m = True
    m_len = len(matrix)
    for i in range(m_len):
        if m_len != len(matrix[i]):
            is_sq_m = is_sq_m and False
    return is_sq_m            
