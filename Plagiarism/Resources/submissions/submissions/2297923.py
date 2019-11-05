def is_unique(l):
    checking = []
    for i in range(0, len(l)):
        if i not in checking:
            checking.append(i)
        else:
            return False
    return True