def is_unique(l):
    for x in l:
        l.count(x)
        if l == []:
            return True
        if l.count(x) == 1:
            return True
        else:
            return False
        
    
    