def shift(l, n):
    shifted_list = []
    n = int(n)
    for i in range(0, len(l)-1):
        x = i + n
        if x < len(l) and x >= 0:
            shifted_list[x] = l[i]
        elif x >= len(l):
            x = x - len(l)
            if x < len(l) >= 0:
                shifted_list[x] = l[i]
            elif x >= len(l):
                x = x - len(l)
                shifted_list[x] = l[i]
        else:
            x = x + len(l)
            if x < len(l) >= 0:
                shifted_list[x] = l[i]
            elif x >= len(l):
                x = x - len(l)
                shifted_list[x] = l[i]
            else:
                x = x + len(l)
                shifted_list[x] = l[i]

    return shifted_list