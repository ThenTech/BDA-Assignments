def is_ordered(l):
    for i in range (1,len(l)):
        if l[i]< l[i-1]:
            return False
        if i+1 == len(l):
            return True