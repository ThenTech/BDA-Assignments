def is_unique(l):
    wrong = 0
    for i in l:
        a = l[:]
        a.del(i)
        for j in a:
            if i == j:
                wrong += 1
    if wrong == 0:
        return True
    else:
        return False





is_unique([1, 2, 3, 4, 5, 6, 7, 8, 9])