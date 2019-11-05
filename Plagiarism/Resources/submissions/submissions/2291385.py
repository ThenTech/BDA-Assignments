def is_ordered(l):
    sortedlist = l.sort()
    for getal in l:
        if l == sortedlist:
            return True
        else:
            return False
