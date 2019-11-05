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


def merge_sort(l):
    result = []
    l = merge_help(l, result)
    for el in l:
        result = merge_lists(el, result)
    return  result

def merge_help(l, result):
    if len(l) == 0:
        return result
    kies = l[0]
    rest = l[1:]
    x = merge_help(rest, result+[[kies]])
    return x
    
merge_sort(input())

