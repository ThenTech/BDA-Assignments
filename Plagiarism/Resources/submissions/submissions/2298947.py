def is_unique(l):
    for i in range(1, len(l)):
        if l[len(l)] == l[len(l) -i-1]:
            return False
    return True