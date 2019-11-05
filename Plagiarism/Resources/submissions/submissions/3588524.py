def merge_lists(first, second):
    if (first[0] < second[0]):
        listNew = first + second
    else:
        listNew = second + first
    return listNew
    
def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        first = l[0:len(l)//2]
        second = l[len(l)//2:len(l)]
        merge_sort(first)
        merge_sort(second)
        l = merge_lists(first, second)
    