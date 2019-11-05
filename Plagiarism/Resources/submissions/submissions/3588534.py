def merge_lists(first, second):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
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
    