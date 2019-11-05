def merge_lists(first, second):
    newList = first + second
    return newList


def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        first = list[:len(list)/2]
        second = list[len(list)/2:]
        merge_sort(first)
        merge_sort(second)
        merge_lists(first, second)