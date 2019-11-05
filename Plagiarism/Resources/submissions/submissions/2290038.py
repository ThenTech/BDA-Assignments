def is_ordered(l):
    for i in l:
        if l[i]>l[i+1]:
            return False