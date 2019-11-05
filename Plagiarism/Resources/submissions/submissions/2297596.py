def is_unique(l):
    if l == []:
        return True
    for x in l:
        if l.count(x) > 1:
            return False
    
    return True
        
    
    