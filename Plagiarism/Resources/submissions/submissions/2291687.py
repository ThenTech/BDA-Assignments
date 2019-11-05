def is_ordered(l):
    for i in range (0,len(l)):
        if l[i+1]< l[i]:
            return False
        if i+1 >= len(l):
            return True