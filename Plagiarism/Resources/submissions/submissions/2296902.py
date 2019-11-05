def is_unique(l):
    uitslag = 0
    for x in range(len(l) - 1):
        for i in range(len(l)):
            if l[x] != l[i]:
                uitslag += 0
            else:
                uitslag += 1
    uitslag = uitslag - (len(l)-1)
    if uitslag == 0:
        return True
    else:
        return False