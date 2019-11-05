def is_unique(l):
    kopielijst = []
    uniek = True
    for el in l:
        if el in kopielijst:
            uniek = False
        if uniek == False:
            return False
        kopielijst.append(el)
    if kopielijst == l:
        return True