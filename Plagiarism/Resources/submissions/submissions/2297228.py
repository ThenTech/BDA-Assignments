def is_unique(list):
    place = 0
    for number in list:
        list_sliced = list[:place] + list[place+1:]
        for figure in list_sliced:
            if number == figure:
                return False
        place = place + 1
    return True

def is_magic_square(matrix):
    sum_hor = 0
    sum_ver = 0
    sum_dia = 0
    k = 0
    l = len(matrix[0]) - 1
    unique_list = []
    sum_list = []

    for list in matrix:
        for number in list:
            unique_list.append(number)

    if len(matrix[0]) % 2 == 0:
        return False
    elif len(matrix) % 2 == 0:
        return False
    elif is_unique(unique_list) == False:
        return False
    else:
        # Horizontal sums
        for list in matrix:
            for number in list:
                sum_hor = sum_hor + number
            sum_list = sum_list + [sum_hor]
            sum_hor = 0

        # Vertical sums
        for j in range(0, len(matrix[0])):
            for list in matrix:
                sum_ver = sum_ver + list[j]
            sum_list = sum_list + [sum_ver]
            sum_ver = 0

        # Diagonal sums
        for list in matrix:
            sum_dia = sum_dia + list[k]
            k = k + 1
        sum_list = sum_list + [sum_dia]
        sum_dia = 0
        for list in matrix:
            sum_dia = sum_dia + list[l]
            l = l - 1
        sum_list = sum_list + [sum_dia]
        sum_dia = 0

        # Checking if all sums are equal
        for i in range(1, len(sum_list)):
            for sum in sum_list:
                if sum_list[i] != sum:
                    return False

        return True