def merge_lists(first, second, l):
    if (first[0] < second[0]):
        l = first + second
    else:
        l = second + first
    return l
def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        first = l[0:len(l)//2]
        second = l[len(l)//2:len(l)]
        merge_sort(first)
        merge_sort(second)
        return(merge_lists(first, second, l))
    