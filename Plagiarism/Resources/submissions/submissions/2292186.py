def is_ordered(l):
    lastnumber = 0
    newnumber = 0
    for i in l:
        if i != 0:
            newnumber = i
            if i < lastnumber:
                lastnumber = newnumber
                return False
        else:
            lastnumber = i
    return True