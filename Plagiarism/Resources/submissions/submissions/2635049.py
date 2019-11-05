import random

def quick_sort(listy):
    if len(listy) <= 1:
        return listy
    r = random.randrange(0,len(listy))
    pivot = listy[r]
    merged_list = []
    listy1 = []
    listy2 = []
    listy3 = []
    for number in listy:
        if number < pivot:
            listy1.append(number)
        elif number == pivot:
            listy2.append(number)
        else:
            listy3.append(number)
    listy1 = quick_sort(listy1)
    listy3 = quick_sort(listy3)
    merged_list = listy1 + listy2 + listy3
    return merged_list
