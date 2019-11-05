def shift(l, n):
    kopie = l[:]
    for el in range(len(l)):
        index_kopie = (el+n)%len(kopie)
        kopie[index_kopie] = l[el]
    return  kopie