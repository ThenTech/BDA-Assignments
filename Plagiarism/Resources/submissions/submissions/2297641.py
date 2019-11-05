def is_magic_square(matrix):
    m = sum_hor(matrix, 0)
    if is_unique(matrix):
        if len(matrix) == len(matrix[0]):
            for x in range(len(matrix)):
                if not sum_hor(matrix, x) == m:
                    return False
            for x in range(len(matrix[0])):
                if not sum_vert(matrix, x) == m:
                    return False

            if not sum_dia(matrix, 'left') == m or not sum_dia(matrix, 'right') == m:
                return False
        else:
            return False
    else:
        return False
    return True

def is_unique(l):
    track_list = []
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] not in track_list:
                track_list.append(l[x][y])
            else:
                return False
    return True


def sum_hor(l, r):
    result = 0
    for i in l[r]:
        result += i
    return result

def sum_vert(l, c):
    result = 0
    for i in range(len(l)):
        result += l[i][c]
    return result

def sum_dia(l, dir='left'):
    result = 0
    for x in range(len(l)):
        if dir == 'left':
            result += l[x][x]
        elif dir == 'right':
            result += l[x][len(l)-x-1]
    return result