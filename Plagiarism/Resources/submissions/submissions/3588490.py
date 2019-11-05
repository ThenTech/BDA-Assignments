def merge_lists(first, second):
    newList = first + second
    return newList


def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        first = l[:len(l)/2]
        second = l[len(l)/2:]
        merge_sort(first)
        merge_sort(second)
        merge_lists(first, second)