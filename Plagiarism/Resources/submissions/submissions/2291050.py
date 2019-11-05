def is_ordered(l):
    vorige = l[0]
    for getal in l:
        if getal >= vorige:
            continue
        else:
            return False
    return True
