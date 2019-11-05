def is_unique(l):
    recent = []
    for i in l:
        if i not in recent:
            recent.append(i)
        else:
            return False
    return True
