def is_magic_square(matrix):
    counterunique = 0
    counterrowsum = 0
    countercolumnsum = 0
    counterdiagonalsum = 0
    A = matrix[:]
    if not len(A) == 3:
        return False
    for i in A:
        matrix.remove(i)
        if i not in matrix:
            counterunique += 1
    if sum(A, [1]) == sum(A, [2]) and sum(A, [1]) == sum(A, [3]):
        counterrowsum += 1
    if sum(i[0] for i in A) == sum(A, [1]):
        countercolumnsum += 1
    if sum(i[1] for i in A) == sum(A, [1]):
        countercolumnsum += 1
    if sum(i[2] for i in A) == sum(A, [1]):
        countercolumnsum += 1
    if A[0][0] + A[1][1] + A[2][2] == sum(A, [1]):
        counterdiagonalsum += 1
    return bool(counterunique > 1 and counterdiagonalsum > 1 and countercolumnsum > 1 and counterrowsum > 1)

