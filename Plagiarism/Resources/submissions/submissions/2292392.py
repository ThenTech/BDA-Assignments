def is_ordered(l):
    length = len(l)
    if length == 0:
        return false
    else:
        lastnumber = l[0]
        newnumber = 0
        for i in l:
            newnumber = i
            if i < lastnumber:
                return False
            else:
                lastnumber = i
        return True