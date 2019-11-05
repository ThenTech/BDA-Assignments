def is_ordered(l):
    for i in l:
        if i == len(l)-1:
            return True
        if int(l[i]) > int(l[i+1]):
            return False



is_ordered([1, 2, 3, 4])
