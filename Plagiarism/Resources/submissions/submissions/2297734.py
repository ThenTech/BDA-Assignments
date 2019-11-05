def is_magic_square(matrix):
    counter = 0
    counterrow = 0
    countercolumn = 0
    counterdiagonal = 0
    l = sum(matrix, [])
    A = l[:]
    if 1 > len(A) < 9:
        return False
    elif len(A) == 1:
        return True
    for i in A:
        l.remove(i)
        if i not in l:
            counter += 1
    if sum(matrix, [0]) == sum(matrix, [1]) and sum(matrix, [1]) == sum(matrix, [2]):
        counterrow += 1
    else:
        return False
    if sum(matrix, [0]) == A[1] + A[4] + A[7] and sum(matrix, [0]) == A[0] + A[3] + A[6]:
        countercolumn += 1
    else:
        return False
    if sum(matrix, [0]) == A[0] + A[4] + A[8]:
        counterdiagonal += 1
    return bool(counter == len(A) and counterrow == 1 and countercolumn == 1 and counterdiagonal == 1)
