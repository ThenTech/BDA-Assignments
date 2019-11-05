def is_ordered(l):
    sortedlist = l[:]
    sortedlist.sort()
    for getal in l:
        if l == sortedlist:
            return True
        elif l == []:
            return True
        else:
            return False
