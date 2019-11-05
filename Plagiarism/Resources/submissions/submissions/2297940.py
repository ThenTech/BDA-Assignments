def is_unique(l):
    checking = []
    for i in l:
        if i not in checking:
            checking.append(i)
        else:
            return False
    return True