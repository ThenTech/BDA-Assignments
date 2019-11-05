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




def merge_sort(listy):
    if len(listy) <= 1:
        return listy
    else:
        listy1 = merge_sort(listy[:len(listy)//2])
        listy2 = merge_sort(listy[len(listy) // 2:])
        return merge_lists(listy1, listy2)
# merge_lists([1, 2, 6], [5,7,8])
# print(merge_sort([8, 1, 5, 7, 2, 4, 6, 9, 10, 3]))