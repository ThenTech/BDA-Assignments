def is_unique(list):
    for x in range(len(list)):
        for y in range(x + 1,len(list)):
            if list[x] == list[y]:
                return False
    return True



def is_magic_square(matrix):
    if is_unique(matrix[0]) and len(matrix) == len(matrix[0]):
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

        z += 1
        sum.append(0)
        for x in range(len(matrix)):
            sum[z] += matrix[x][len(matrix) - x - 1]

        check = sum[0]
        for x in sum:
            if x != check:
                return False
        return True
    else:
        return False