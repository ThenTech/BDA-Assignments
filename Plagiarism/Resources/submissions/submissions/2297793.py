def is_unique(l):
    checking = []
    for i in l:
        checking.append(i)
        if i is checking:
            return False
    return True
        
        