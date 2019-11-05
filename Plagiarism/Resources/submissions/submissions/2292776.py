def shift(l, n):
    p=[]
    for i in range (0,len(l)):
        x = i-n
        while x >= len(l):
            x -= len(l)
        while x<0:
            x += len(l)
        p.append (l[x])
    return p