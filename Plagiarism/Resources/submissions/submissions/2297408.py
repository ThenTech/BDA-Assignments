def is_unique(l):
    b = l[:]
    for i in range(0, len(l)):
        if b.count(l)>1:
            return False7
        elif l == []:
            return False
        return True
    
        
        