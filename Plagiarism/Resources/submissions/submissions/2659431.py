def is_magic_square(matrix):
    n = sum(l[0])
    l = len(matrix)
    if horizotaal(matrix ,n )== False or verticaal(matrix,n)==False or schuin(matrix,n)==False or rijen(matrix,l == False):
        return False
    return True

def rijen(matrix, l):
    if len(matrix)%2 == 0:
        return False
    for i in range(len(matrix)):
        if len(i)!= l:
            return False
    
def horizontaal(matrix,n):
    for i in matrix:
        p = 0
        for j in i:
            p += j
        if p != n:
            return False
def verticaal(matrix,n):
    for i in matrix:
        p=0
        for j in matrix:
            p += matrix[i][j]
        if p != n:
            return False
def schuin(matrix,n):
    p=0
    for i in matrix:
        p += matrix[i][i]
        s += matrix[len(matrix)-1-i][len(matrix)-i-1]
        if q!=n or s!= n:
            return False
        