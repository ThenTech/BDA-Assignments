def merge_lists(first, second):
    i = 0
    j = 0
    merged_list = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            merged_list.append(first[i])
            i += 1
        else:
            merged_list.append(second[j])
            j += 1
    for k in range(i, len(first)):
        merged_list.append(first[k])
    for u in range(j, len(second)):
        merged_list.append(second[u])
    return merged_list



def merge_sort(listy):
    if len(listy) <= 1:
        return listy
    else:
        listy_1 = listy[:len(listy) // 2]
        listy_2 = listy[len(listy) // 2:]
        if len(listy_1) > 1:
            listy_1 = merge_sort(listy_1)
        if len(listy_2) > 1:
            listy_2 = merge_sort(listy_2)
    return merge_lists(listy_1,listy_2)
