def shift(l, n):
    
    if l == []:
        return l
    else:
        n = n % (len(l))
        kopielijst = l[:]
        plaats = -1
        for getal in l:
            plaats += 1
            nieuweplaats = (plaats+n)
            if nieuweplaats>(len(l)-1):
                nieuweplaats = nieuweplaats - len(l)
            kopielijst[nieuweplaats] = l[plaats]
        return kopielijst
shift([1, 2, 3, 4, 5], -2)