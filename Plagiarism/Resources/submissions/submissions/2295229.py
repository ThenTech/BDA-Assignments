def is_ordered(l):
    givenlist = l[:]
    givenlist.sort()
    return givenlist[l] == givenlist.sort()