def quick_sort(l, sorted_list=None, length_history=None):
    if sorted_list is None:
        sorted_list = []
        length_history = []

    length_history.append(len(l))
    half_len = int(len(l) / 2)
    l_less = []
    l_equal = []
    l_greater = []

    if len(l) > 1:
        pivot = l[half_len]
        for number in l:
            if number < pivot:
                l_less.append(number)
            elif number > pivot:
                l_greater.append(number)
            else:
                l_equal.append(number)
    else:
        return l

    l1 = quick_sort(l_less, sorted_list, length_history)
    if not is_empty(l1) and not is_sorted(length_history, sorted_list):
        sorted_list.append(l1[0])

    l2 = l_equal
    if not is_empty(l2):
        for i in range(len(l2)):
            sorted_list.append(l2[i])

    l3 = quick_sort(l_greater, sorted_list, length_history)
    if not is_empty(l3) and not is_sorted(length_history, sorted_list):
        sorted_list.append(l3[0])

    # print(len(sorted_list), '/', length_history[0], 'Sorted:', sorted_list, length_history[0] == len(sorted_list))

    if is_sorted(length_history, sorted_list):
        return sorted_list


def is_empty(l):
    if l is None or len(l) == 0:
        return True
    return False


def is_sorted(length_history, sorted_list):
    if length_history[0] == len(sorted_list):
        return True
    return False