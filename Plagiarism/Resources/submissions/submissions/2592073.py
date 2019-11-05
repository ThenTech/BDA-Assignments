def dimension_checker(mx):
    if len(mx) % 2 == 0:
        return False
    
    for i in range(len(mx)):
        if len(mx) != len(mx[i]):
            return False
    

def unique(list):
    check = []
    for ch in list:
        if ch in check:
            return False
        else:
            check.append(ch)
    return True

def twod_1d(mx):
    list = []
    for r in mx:
        for el in r:
            list.append(el)
    return list

def som(mx):
    s = 0
    for i in range(len(mx)):
        s += mx[i][i]
    checksum = s
    
    for i in range(len(mx)):
        s1 = 0
        s2 = 0
        for j in range(len(mx)):
            s1 += mx[i][j]
            s2 += mx[j][i]
        if s1 != checksum or s2 != checksum:
            return False
    return True

def is_magic_square(matrix):
    return dimension_checker (matrix) and unique(twod_1d(matrix)) and som(matrix)