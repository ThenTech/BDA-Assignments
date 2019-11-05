def is_unique(l):
    for i in range(0, len(l)):
        if l.count(i)>1:
            return False
        return True
    
        
        