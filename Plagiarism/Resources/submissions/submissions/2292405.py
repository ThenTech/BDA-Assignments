def shift(l, n):
    p=[]
    for i in range (0,len(l)):
        x = len(l)-n-1-i
        while x >= len(l):
            x -= len(l)
        p.append (l[x])
    return p