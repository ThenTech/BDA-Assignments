def shift(l, n):
    if len(l) == 0:
        return l
    new_list = []
    begin_getal = len(l) - n
    begin_getal = begin_getal % len(l)

    for i in l[begin_getal:]:
        new_list.append(i)
        l.remove(i)

    for j in l:
        new_list.append(j)

    return new_list