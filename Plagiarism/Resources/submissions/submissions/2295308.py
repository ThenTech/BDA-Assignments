def is_ordered(l):
    givenlist = l[:]
    givenlist.sort()
    return givenlist() == givenlist.sort()