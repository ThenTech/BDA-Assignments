def is_unique(l):
    wrong = 0
    for i in l:
        x = 0
        a = l[:]
        x += 1
        for j in a:
            if i == j:
                wrong += 1
    if wrong == len(l):
        return True
    else:
        return False




print(is_unique([1, 2, 3, 4, 1, 6, 7, 8, 9]))