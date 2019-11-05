def is_ordered(l):
    for i in range(1, len(l)):
        return l[i] <= l[i+1] or l[i] >= l[i+1] == 0