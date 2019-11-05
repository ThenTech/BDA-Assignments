def is_ordered(l):
    kopie = l[:]
    kopie.sort()
    if kopie == l:
        return True
    else:
        return False