def is_ordered(l):
    lastnumber = 0
    newnumber = 0
    everythingCorrect = True
    for i in l:
        newnumber = i
        if i < lastnumber:
            return False
        lastnumber = newnumber
    return True