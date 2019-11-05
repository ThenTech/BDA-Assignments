def is_ordered(l):
    lastnumber = l[0]
    newnumber = 0
    length = len(l)
    if lenght == 0:
        return false
    else:
        for i in l:
            newnumber = i
            if i < lastnumber:
                return False
            else:
                lastnumber = i
        return True