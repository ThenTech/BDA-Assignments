def is_magic_square(matrix):
    counter = 0
    counterrow = 0
    l = sum(matrix, [])
    A = l[:]
    if 1 < len(A) < 9:
        return False
    elif len(A) == 1:
        return True
    for i in A:
        l.remove(i)
        if i not in l:
            counter += 1
    if A[0] + A[1] + A[2] == A[3] + A[4] + A[5] and A[3] + A[4] + A[5] == A[6] + A[7] + A[8]:
        counterrow += 1
    else:
        return False
    return bool(counter == len(A) and counterrow == 1)

