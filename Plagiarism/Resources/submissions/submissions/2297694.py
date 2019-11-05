def shift(l, n):
    n = n % (len(l))
    kopielijst = l[:]
    plaats = -1
    for getal in l:
        plaats += 1
        nieuweplaats = (plaats+n)
        if nieuweplaats>(len(l)-1):
            nieuweplaats = nieuweplaats - len(l)
        kopielijst[nieuweplaats] = l[plaats]
    print(kopielijst)
shift([1, 2, 3, 4, 5], -2)