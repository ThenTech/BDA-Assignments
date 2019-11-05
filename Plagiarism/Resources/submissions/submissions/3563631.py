def is_magic_square(matrix):

    sum1 = 0
    sum2 = 0

    test = False

    test2 = True

    numbers = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            numbers += [matrix[i][j]]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in numbers:
                test2 = False

    for i in range(len(matrix)):
        if len(matrix) == len(matrix[i]):
            test = True

    if test == True and test2 == True:

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == j:
                    sum1 += matrix[i][j]



        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i + 1 == -(j-len(matrix)):                       #i begint te tellen bij 0 !!!!, negatief begint bij 1 !!!!
                    sum2 += matrix[i][j-len(matrix)]


        return bool(sum1 == sum2)

    else:
        return False