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
    end = 0
    for i in range(len(listy)-1):
        if listy[i] <= listy[i+1]:
            end += 1
        else:
            end += 1
            break
    return merge_sort_helper(listy, 0, end)

def merge_sort_helper(listy, start, end):
    if len(listy) == len(listy[start:end]):
        return listy
    listy1 = listy[start:end]
    start = end
    if len(listy[start:]) != 1:
        for i in range(start, len(listy)-1):
            if listy[i] <= listy[i+1]:
                end += 1
            else:
                end += 1
                break
        listy2 = listy[start:end]
        merged_listy = merge_lists(listy1, listy2)
        listy = merged_listy+listy[end:]
        return merge_sort_helper(listy, 0, end)
    else:
        listy2 = listy[start:]
        merged_listy = merge_lists(listy1, listy2)
        return merge_sort_helper(merged_listy, 0, len(merged_listy))