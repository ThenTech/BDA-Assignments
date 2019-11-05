def is_unique(l):
    for i in range(0, len(l)):
        if l.count(l)>1:
            return False
        return True
        
        