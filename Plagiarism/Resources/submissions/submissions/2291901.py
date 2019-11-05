def is_ordered(l):
    lastnumber = 0
    newnumber = 0
    everythingCorrect = True
    for i in l:
        if i != 0:
            newnumber = i
            if i < lastnumber:
                return False
            lastnumber = newnumber
        else:
            lastnumber = newnumber
    return True