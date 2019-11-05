def is_ordered(l):
    lastnumber = l[0]
    newnumber = 0
    for i in l:
        newnumber = i
        if i < lastnumber:
            return False
        else:
            lastnumber = i
    return True