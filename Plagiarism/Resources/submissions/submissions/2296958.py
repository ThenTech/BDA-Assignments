def is_ordered(l):
    for i in l:
        if i[l] < i[l+1]:
            return True
        else:
            return False