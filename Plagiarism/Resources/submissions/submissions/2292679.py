def is_unique(list):
    a = 1
    for j in list:
        for i in list[a:]:
            if j != i:
                continue
            elif j == i:
                return False
        a += 1
    return True