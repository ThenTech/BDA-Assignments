pivotten = []
def quick_sort(l):
    for i in range(len(l)):
        l = sort(l, i)
    return l

def sort(l, i):
    if l == []:
        return l
    lgd = []
    lkd = []
    lga = []
    r = i
    for i in l:
        if i > l[r]:
            lgd.append(i)
        if i < l[r]:
            lkd.append(i)
        if i == l[r]:
            lga.append(i)
    lijst = lkd + lga + lgd
    return lijst