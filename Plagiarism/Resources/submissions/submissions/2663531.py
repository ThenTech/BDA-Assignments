def merge_lists(first, second):
    indexfirst = 0
    indexsecond = 0
    lijst = []
    for i in range(len(first)):
        if first[indexfirst] <= second[indexsecond]:
            lijst.append(first[indexfirst])
            indexfirst += 1
        else:
            lijst.append(second[indexsecond])
    return lijst


def merge_sort(l):
    pass