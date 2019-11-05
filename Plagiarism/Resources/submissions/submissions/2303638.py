def is_magic_square(m):
    total = 0
    ismagic = True

    for i in m[0]:
        total += i

    for i in range(len(m)):
        totalnew = 0
        for j in m[i]:
            totalnew += j
        if totalnew != total:
            ismagic = False
            break

    for i in range(len(m)):
        totalnew = 0
        for j in range(len(m[i])):
            totalnew += m[i][j]
        if totalnew != total:
            ismagic = False
            break

    totalnew = 0
    count = 0

    for i in range(len(m)):
        totalnew += m[i][count]
        count += 1
    if totalnew != total:
        ismagic = False

    totalnew = 0
    count = len(m) - 1

    for i in range(len(m)):
        totalnew += m[i][count]
        count -= 1
    if totalnew != total:
        ismagic = False

    if ismagic:
        return True
    else:
        return False