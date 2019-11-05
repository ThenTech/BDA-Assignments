def merge_lists(first, second):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(first) and right_index < len(second):
        if first[left_index] < second[right_index]:
            result.append(first[left_index])
            left_index += 1
        else:
            result.append(second[right_index])
            right_index += 1

    result += first[left_index:]
    result += second[right_index:]
    return result
    
def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        first = l[0:len(l)//2]
        second = l[len(l)//2:len(l)]
        merge_sort(first)
        merge_sort(second)
        l = merge_lists(first, second)
        return l
    