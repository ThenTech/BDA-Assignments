def quick_sort(l):
    if len(l) > 1:
        p = l[0]
        smaller = []
        same = []
        bigger = []
        for i in l:
            if i < p:
                smaller += [i]
            elif i > p:
                bigger += [i]
            else:
                same += [i]
        list = quick_sort(smaller) + same + quick_sort(bigger)
        return list
    else:
        return l
        