def merge_lists(first, second):
    merged_listy = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged_listy += [first[i]]
            i += 1
        elif second[j] <= first[i]:
            merged_listy =  merged_listy + [second[j]]
            j += 1
    if i == len(first):
        merged_listy += second[j:]
    else:
        merged_listy += first[i:]
    return merged_listy

def merge_sort(li):
    if (len(li) <= 1):
        return li
    elif(len(li) > 1):
        l1 = merge_sort(li[:len(li)//2])
        l2 = merge_sort(li[len(li)//2:])
        return merge_lists(l1, l2)
