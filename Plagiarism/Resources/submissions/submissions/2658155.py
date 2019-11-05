import random


def quick_sort2(listy):
    if len(listy) <= 1:
        return listy
    r = random.randrange(0, len(listy))
    pivot = listy[r]

    # swap
    listy[r], listy[(len(listy) - 1)] = listy[(len(listy) - 1)], listy[r]

    # track numbers < pivot
    swap_element = 0
    for i in range(0, len(listy)-1):
        if listy[i] < pivot:
            small_number = listy[i]
            listy[i] = listy[swap_element]
            listy[swap_element] = small_number
            swap_element += 1
        else:
            continue

    # swap
    listy[swap_element], listy[(len(listy) - 1)] = listy[(len(listy) - 1)], listy[swap_element]
    
    listy1 = quick_sort2(listy[:swap_element])
    listy2 = quick_sort2(listy[swap_element:])
    return listy1+listy2


def quick_sort(listy):
    return quick_sort2(listy)