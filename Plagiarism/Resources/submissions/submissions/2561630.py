def merge_lists(first, second):
    output = []

    if not first:
        return second
    if not second:
        return first

    total = len(first) + len(second)
    while True:
        if len(first) == 0:
            output.extend(second)
            break
        elif len(second) == 0:
            output.extend(first)
            break

        if first[0] < second[0]:
            output.append(first[0])
            first = first[1:]
        else:
            output.append(second[0])
            second = second[1:]

    return output


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return l
    else:
        mid = n // 2
        l1 = l[:mid]
        l2 = l[mid:]
        return merge_lists(merge_sort(l1), merge_sort(l2))
