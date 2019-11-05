def check(mx):
    count = 0
    tot_count = 0
    for row in mx:
        for element in row:
            tot_count += 1
        count += 1
    if len(mx) != count or tot_count // len(mx) != len(mx):
        return False

    elems = []
    for row in mx:
        for element in row:
            if element not in elems:
                elems.append(element)
            else:
                return False

    return True


def magic(mx):
    n = len(mx)
    half = n // 2
    magic_number_hor = 0
    for i in range(n):
        magic_number_hor += mx[half][i]

    magic_number_ver = 0
    for i in range(n):
        magic_number_ver += mx[i][half]

    magic_number_dial = 0
    for i in range(n):
        magic_number_dial += mx[i][i]

    magic_number_diar = 0
    for i in range(n):
        magic_number_diar += mx[n-i-1][i]

    if magic_number_hor == magic_number_ver == magic_number_dial == magic_number_diar:
        return True
    return False


def is_magic_square(matrix):
    if check(matrix) and magic(matrix):
        return True
    return False