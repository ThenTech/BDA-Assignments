def merge_lists(l1, l2):
    new_list = []
    while True
        if l1 == [] or l2 == []
            new_list += l1+l2
            return new_list
        if l1[0] > l2[0]:
            new_list += [l2[0]]
        else:
            new_list += [l1[0]]


def merge_sort(l):
    if len(l) > 1:
        l1 = merge_sort(l[:len(l)//2])
        l2 = merge_sort(l[(len(l)//2)+1:])
        return merge_lists(l1, l2)
    else:
        return l