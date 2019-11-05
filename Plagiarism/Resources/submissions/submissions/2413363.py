def quick_sort(l):
    if len(l) > 2:
        pivot = len(l)//2
        list1 = l[:len(l)//2]
        list2 = l[len(l)//2+1:]
        list1 = quick_sort(list1)
        list2 = quick_sort(list2)
        pivotlist = []
        pivotlit.append(pivot)
        return(list1 + pivot + list2)
    l.sort()
    return l
    