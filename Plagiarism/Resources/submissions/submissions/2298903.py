def is_unique(l):
    for i in range(1, len(l)):
        if l[len(l)] == l[len(l) -i]:
            return False
    return True