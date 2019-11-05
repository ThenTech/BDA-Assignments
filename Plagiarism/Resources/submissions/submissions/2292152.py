def is_unique(l):
    teller1 = 0
    for i in l:
        teller2 = 0
        for j in l:
            if teller1 != teller2 and i == j:
                return False
            else:
                teller2 += 1
        teller1 += 1
    return True