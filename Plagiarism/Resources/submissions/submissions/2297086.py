def shift(l, n):
    newl = []
    for i in range(len(l)-n+1, len(l)):
        newl.append(l[i])
    for i in range(len(l)-n+1):
        newl.append(l[i])
    return newl