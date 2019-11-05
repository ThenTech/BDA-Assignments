def merge_lists(first, second):
    if (first[0] < second[0]):
        newList = first + second
    else:
        newList = second + first
    return newList


def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        first = l[0:len(l)//2]
        second = l[len(l)//2:len(l)]
        merge_sort(first)
        merge_sort(second)
        return(merge_lists(first, second))
    