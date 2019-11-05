def is_ordered(l):
    for i in l:
        return l[i] >= l[i-1] or l[i-1] >= l[i+1] == 0
        