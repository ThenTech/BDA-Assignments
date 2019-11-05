def is_unique(l):
    if l.count(l)>1:
        return False
    elif l == []:
        return False
    return True
    
        
        