def is_ordered(l):
    sortedlist = l[:]
    sortedlist.sort()
    if l == []:
            return True
    for getal in l:
        if l == sortedlist:
            return True
        
        else:
            return False
