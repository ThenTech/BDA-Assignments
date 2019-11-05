import random

def quick_sort(listy):
    if len(listy) <= 1:
        return listy
    p = random.randrange(0, len(listy))
    pivot = listy[p]
    sorted_listy = []
    listy_1 = []
    listy_2 = []
    listy_3 = []
    for i in listy:
        if i < pivot:
            listy_1.append(i)
        elif i == pivot:
            listy_2.append(i)
        else:
            listy_3.append(i)
    listy_1 = quick_sort(listy_1)
    listy_3 = quick_sort(listy_3)
    sorted_listy = listy_1 + listy_2 + listy_3
    return sorted_listy