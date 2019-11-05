def quick_sort(l):
    sortedlist = []
    small = []
    equal = []
    big = []
    if len(l) > 1:
        p = l[0]
        for i in l:
            if int(i) < p:
                small.append(i)
            elif int(i) > p:
                big.append(i)
            else:
                equal.append(i)
        sortedlist += quick_sort(small) + equal + quick_sort(big)
        return sortedlist
    else:
        return l