def is_ordered(l):
    givenlist = l[:]
    newlist = givenlist.sort()
    if givenlist == is_ordered(l) :
        True
    else:
        ()
