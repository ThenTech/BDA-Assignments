def is_ordered(l):
    givenlist = l[:]
    givenlist.sort()
    return True if givenlist == givenlist.sort()