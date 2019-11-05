from random import *


def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        p = l[randint(0, len(l) - 1)]
        less = []
        more = []

        for i in l:
            if i < p:
                less.append(i)
            elif i > p:
                more.append(i)

        return quick_sort(less) + [p] + quick_sort(more)
