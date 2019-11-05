def is_unique(l):
    for i in range(0, len(l)):
        if i<l[i+1]:
            return True
        return False