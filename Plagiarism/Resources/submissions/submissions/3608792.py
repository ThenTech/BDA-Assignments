def merge_lists(first, second):
    if len(first) == 0:
        return second
    if len(second) == 0:
        return first
    
    list = []
    sec = 0
    for i in range(len(first)):
        while second[sec] <= first[i]:
            list.append(second[sec])
            sec += 1
            if sec == len(second):
                break
        list.append(first[i])
        if sec == len(second):
            for j in range(i+1, len(first)):
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