def is_unique(l):
    for i in l:
        for j in l:
            if i == j:
                return False
            else:
                return True