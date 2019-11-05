def quick_sort(l):
    p = l[int(len(l)/2)]
    less = []
    equal = []
    more = []
    result = []
    for i in l:
        if i < p:
            result += less.append(i)
        elif i == p:
            equal.append(i)
        elif i > p:
            result += more.append(i)
    result.append(equal)
    return result