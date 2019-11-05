import random
pivotten = []
def quick_sort(l):
    if l == []:
        return l
    lgd = []
    lkd = []
    lga = []
    r = random.randrange(0, len(l))
    while r in pivotten:
        r = random.randrange(0, len(l))
    pivotten.append(r)
    for i in l:
        if i > l[r]:
            lgd.append(i)
        if i < l[r]:
            lkd.append(i)
        if i == l[r]:
            lga.append(i)
    lijst = lkd + lga + lgd
    if len(pivotten) < len(l):
        lel = quick_sort(lijst)
        return lel
    else:
        return lijst
