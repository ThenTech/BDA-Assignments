def is_magic_square(matrix):
    sum = []
    z = -1
    for y in matrix:
        z+=1
        sum.append(0)
        for x in y:
            sum[z] += x
    z += 1
    sum.append(0)
    for x in range(len(matrix)):
        sum[z] += matrix[x][x]
    for x in sum:
    if x != check:
        return False

    z += 1
    sum.append(0)
    for x in range(len(matrix)):
        sum[z] += matrix[x][len(matrix) - x - 1]

    check = sum[0]
    for x in sum:
        if x != check:
            return False
    return True