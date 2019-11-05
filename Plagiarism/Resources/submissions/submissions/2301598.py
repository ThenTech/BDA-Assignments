def shift(l, n):
    kopie = l[:]
    for i in range(len(l)):
        index_kopie = (i + n) % len(kopie)
        kopie[index_kopie] = l[i]
    return kopie