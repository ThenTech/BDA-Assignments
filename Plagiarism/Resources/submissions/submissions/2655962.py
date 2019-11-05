import random


def quick_sort2(listy, x, y):
    if x <= y <= -1 or len(listy) <= 1:
        return listy
    r = random.randrange(0, len(listy))
    pivot = listy[r]

    # swap
    listy[r] = listy[(len(listy) - 1)]
    listy[(len(listy) - 1)] = pivot

    # track numbers < pivot
    swap_element = 0
    for i in range(0, len(listy)):
        if listy[i] < pivot:
            small_number = listy[i]
            listy[i] = listy[swap_element]
            listy[swap_element] = small_number
            swap_element += 1
        else:
            continue

    # swap
    listy[(len(listy) - 1)] = listy[swap_element]
    listy[swap_element] = pivot
    if swap_element == 0:
        swap_element = -1
    listy1 = quick_sort2(listy[:swap_element], 0, swap_element)
    listy2 = quick_sort2(listy[swap_element:], swap_element, len(listy) - 1)

    return listy1 + listy2


def quick_sort(listy):
    return quick_sort2(listy, 0, len(listy))