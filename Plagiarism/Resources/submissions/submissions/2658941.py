def merge_list(l1, l2):
    i, x = 0, 0

    while i < len(l1):
        if x == len(l2):
            break
        if l1[i] > l2[x]:
            l1[i:i] = [l2[x]]
            i += 1
            x += 1
        else:
            i += 1
    l1 = l1[:] + l2[x:]
    return l1


def merge_sort(l):
    half_len = int(len(l)/2)
    l1 = l[:half_len]
    l2 = l[half_len:]

    if len(l) != 1 and len(l) != 0:
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
    merged_list = merge_list(l1, l2)
    return merged_list