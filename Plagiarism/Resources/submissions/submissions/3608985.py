def is_unique(l):
        for i in range(0, len(l)):
        number = l[i]
        for j in range(i + 1, len(l)):
            if(number == l[j]):
                return False

    return True