def is_magic_square(matrix):
    lijst = []
    som = 0
    endnow = 0
    m = 0
    for i in matrix:
        for j in i:
            som += j
            if j in lijst:
                endnow += 1
            lijst.append(j)
        if m == 0:
            m = som
        if m != som:
            endnow += 1
        som = 0
        if endnow != 0:
            return False
    if len(lijst) % 2 == 0:
        return False
    return True