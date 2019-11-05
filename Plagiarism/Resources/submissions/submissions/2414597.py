def quick_sort(l):
    result = []
    if len(l)>1:
        p = l[int(len(l)/2)]
        less = []
        equal = []
        more = []
        for i in l:
            if i < p:
                less.append(i)
            elif i == p:
                equal.append(i)
            elif i > p:
                more.append(i)
        result += quick_sort(less)
        result += equal
        result += quick_sort(more)
    else:
        result += l
    return result