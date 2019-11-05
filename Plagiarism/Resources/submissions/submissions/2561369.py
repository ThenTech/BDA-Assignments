def merge_lists(first, second):
    output = []
    for i in first:
        output.append(i)
    for i in second:
        output.append(i)
    return sorted(output)


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return l
    else:
        mid = n // 2
        l1 = l[:mid]
        l2 = l[mid:]
        return merge_lists(merge_sort(l1), merge_sort(l2))
