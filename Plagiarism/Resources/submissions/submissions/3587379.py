def is_unique(l):
    uniqueList = []
    
    for i in l:
        if i in uniqueList:
            return False
        else:
            uniqueList.append(i)
    return True