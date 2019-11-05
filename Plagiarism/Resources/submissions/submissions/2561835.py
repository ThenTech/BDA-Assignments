import random


def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        p = l[random.randint(0, len(l) - 1)]
        less = []
        equal = []
        more = []

        for i in l:
            if i < p:
                less.append(i)
            elif i > p:
                more.append(i)
            else:
                equal.append(i)

        return quick_sort(less) + equal + quick_sort(more)
