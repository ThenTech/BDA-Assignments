def is_unique(l):
    checking = []
    for i in range(0, len(l)):
        if i is not in checking:
            checking.append(i)
            return True
        else:
            return False
        
        