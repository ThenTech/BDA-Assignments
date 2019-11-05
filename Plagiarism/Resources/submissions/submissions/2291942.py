def is_unique(l):
    for i in range(len(l)):
        count = 0
        x = l[i]
        for j in range(len(l)):
            if l[j] == x:
                count = count + 1
            elif count == 2:
                return False
    return True