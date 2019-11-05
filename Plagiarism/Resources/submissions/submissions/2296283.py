def is_unique(l):
    teller = -1
    kopie = l[:]
    kopie2 = []
    for element in l:
        teller += 1
        if  element in kopie and element not in kopie2:
            del kopie[teller]
            kopie2.append(element)
            teller = teller - 1
            continue
        elif element in kopie2:
            return False
    return True