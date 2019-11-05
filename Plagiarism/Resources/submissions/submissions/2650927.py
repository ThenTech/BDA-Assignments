def is_magic_square(matrix):
    good_sum = 0
    sum = 0

    for a in matrix[0]:
        good_sum += a

    for b in range(0, len(matrix)):
        sum = 0
        for c in range(0, len(matrix[b])):
            sum += matrix[b][c]
        if good_sum != sum:
            return False

    for d in range(0, len(matrix)):
        sum = 0
        for e in range(0, len(matrix[d])):
            sum += matrix[e][d]
        if good_sum != sum:
            return False

    sum = 0
    for f in range(0, len(matrix)):
        for g in range(0, len(matrix[f])):
            if f == g:
                sum += matrix[f][g]
    if good_sum != sum:
        return False

    sum = 0
    for h in range(0, len(matrix)):
        sum += matrix[h][len(matrix) - h - 1]
    if good_sum != sum:
        return False

    return True

