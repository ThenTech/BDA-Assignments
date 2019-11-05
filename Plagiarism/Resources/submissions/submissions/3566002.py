def quick_sort(l):
    if l:
        pivot = l[0]
        below = [i for i in l[1:] if i < pivot]
        above = [i for i in l[1:] if i >= pivot]
        return quick_sort(below) + [pivot] + quick_sort(above)
    return l