def merge_lists(first, second):
    if len(first) == 0:
        return second
    if len(second) == 0:
        return first
    
    list = []
    sec = 0
    for i in first:
        while second[sec] <= i:
            list.append(second[sec])
            sec += 1
            if sec == len(second):
                break
        list.append(i)
        if sec == len(second):
            for j in range(i, len(first)):
                list.append(first[j])
            break
    if sec != len(second):
        for i in range(sec, len(second)):
            list.append(second[i])
    return list
    


def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        half = len(l)//2
        l1 = l[:half]
        l2 = l[half:]
        return merge_lists(merge_sort(l1), merge_sort(l2))