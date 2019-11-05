sorted_list = []
length_history = []

def quick_sort(l):
    global sorted_list
    global length_history
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
        # print(l_less, len(l_less) == 1, l_equal, len(l_equal) == 1, l_greater, len(l_greater) == 1)
    else:
        return l

    l1 = quick_sort(l_less)
    if l1 is not None and len(l1) != 0:
        sorted_list.append(l1[0])

    l2 = l_equal
    if len(l2) == 1:
        sorted_list.append(l2[0])
    elif len(l2) >= 1:
        for number in l2:
            sorted_list.append(number)

    l3 = quick_sort(l_greater)
    if l3 is not None and len(l3) != 0:
        sorted_list.append(l3[0])

    if l3 is not None and length_history[0] == len(l3):
        sorted_list = []
        return l3
    #print(len(sorted_list), '/', length_history[0], 'Sorted:', sorted_list, length_history[0] == len(sorted_list))
    if length_history[0] == len(sorted_list):
        private_sorted_list = sorted_list[:]
        sorted_list = []
        return private_sorted_list