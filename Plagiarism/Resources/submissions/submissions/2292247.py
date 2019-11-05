def is_unique(l):
    dubbel = False
    juist = True
    for n in range(len(l)):
        for k in range(len(l)):
            if not n == k:
                if l[n] == l[k]:
                    juist = False
                    dubbel = True
        if dubbel == True:
            break
    if juist == False:
        return False
    else:
        return True