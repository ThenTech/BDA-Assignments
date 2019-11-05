def is_unique(l):
    lijst =[]
    for x in range(len(l)-1):
        lijst.append(x)
        if lijst in l:
            return False
    return True
