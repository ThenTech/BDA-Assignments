def quick_sort(l):
    result = []
    if len(l)>1:
        p = l[int(len(l)/2)]
        less = []
        equal = []
        more = []
        for i in l:
            if i < p:
                less.append(quick_sort(i))
            elif i == p:
                equal.append(i)
            elif i > p:
                more.append(quick_sort(i))
        result += less
        result += equal
        result += more
    else:
        result += l
    return result