def is_unique(l):
    for item in l:
        matchcounter = 0
        for item2 in l:
            if item == item2:
                matchcounter += 1
        if matchcounter > 1:
            return False
    
    return True