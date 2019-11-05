def shift(l, n):
    hulp =[]
    for i in range(len(l)):
        hulp.append(i)
    for i in range(len(l)):
        if i+n < len(l):
            hulp[i + n] = l[i]
        elif i+n >= len(l):
            hulp[(i + n) % len(l)] = l[i]

    return hulp