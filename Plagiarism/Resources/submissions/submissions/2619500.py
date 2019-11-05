def merge_lists(first, second):
    sorteer = []
    if len(first) == 0:
        for el in second:
            sorteer.append(el)
            return sorteer
    if len(second) == 0:
        for el in first:
            sorteer.append(el)
            return sorteer
    if len(first) > len(second):
        lengte_kleinste = len(second)
    else:
        lengte_kleinste = len(first)

    een = 0
    twee = 0
    while True:
        if first[een] < second[twee]:
            sorteer.append(first[een])
            een = een + 1
        else:
            sorteer.append(second[twee])
            twee = twee + 1
        if een == len(first) or twee == len(second):
            break


    if een < len(first):
        for el in range(een, len(first)):
            sorteer.append(first[el])
    else:
        for el in range(twee, len(second)):
            sorteer.append(second[el])

    return sorteer




def quick_sort(l):
    return pivot(l)

def pivot(l):
    pivot_index = len(l)//2
    pivot_waarde = l[pivot_index]
    small = []
    eq = []
    great = []
    for el in l:
        if el < pivot_waarde:
            small.append(el)
        elif el == pivot_waarde:
            eq.append(el)
        else:
            great.append(el)
    small = merge_lists(small,[])
    great = merge_lists([great],[])
    alles = small + eq + great
    return alles

