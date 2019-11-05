def is_ordered(l):
    for i in range(0, len(l)):
        return l[i] <= l[i+1] or l[i] >= l[i+1] == 0