magic_square = []


def check_diag1(l, n):

    sum = 0
    for i in range(0,len(l)):
        sum += l[i][i]

    return sum == n


def check_diag2(l, n):

    sum = 0
    for i in range(0,len(l)):
        sum += l[i][len(l)-i-1]

    return sum == n


def check_cols(l, n):

    for j in range(0,len(l)):
        sum = 0
        for i in range(0,len(l)):
            sum += l[i][j]

        if sum != n:
            return False

    return True


def check_rows(l, n):

    for i in range(0,len(l)):
        sum = 0
        for j in range(0,len(l)):
            sum += l[i][j]

        if sum != n:
            return False

    return True


def check_dimensions(l):
    # number of rows should be uneven
    if len(l) % 2 == 0:
        return False

    n = len(l)

    # every column should have length n
    for i in range(0,n):
        if len(l[i]) != n:
            return False

    return True


def check_unique(l):
    # transform to 1D list
    l1d = []
    for row in l:
        for item in row:
            l1d.append(item)

    # use previously created is_unique function for 1D lists
    return is_unique(l1d)


def is_unique(l):
    # for all combinations
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            # check if they are different
            if i != j and l[i] == l[j]:
                return False

    return True


def is_magic_square(l):

    if not check_dimensions(l) or not check_unique(l):
        return False

    n = sum(l[0])
    return check_rows(l,n) and check_cols(l,n) and check_diag1(l,n) and check_diag2(l,n)

