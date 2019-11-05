def shift(l, n):
    newl = []
    for i in range(len(l)-n, len(l)):
        newl.append(l[i])
    for i in range(len(l)-n):
        newl.append(l[i])
    return newl

