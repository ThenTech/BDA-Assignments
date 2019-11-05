def quick_sort(l):
    p = l[int(len(l)/2)]
    less = []
    equal = []
    more = []
    result = []
    for i in l:
        if i < p:
            less.append(i)
        elif i == p:
            equal.append(i)
        elif i > p:
            more.append(i)
    result += less
    result += equal
    result += more
    return result