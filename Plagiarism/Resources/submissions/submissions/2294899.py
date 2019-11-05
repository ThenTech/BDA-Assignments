def is_unique(l):
    for element1 in l:
        for element2 in l:
            if element1 == element2:
                return False
    return True