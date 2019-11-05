def verplaatsingrechts(l):
    k = l + []
    for i in range(len(l)):
        if i-1 < 0:
            k[i] = l[len(l-1)]
        else:
            k[i] = l[i-1]
    return k

def verplaatsinglinks(l):
    k = l + []
    for i in range(len(l)):
        if i+1 >= len(l):
            k[i] = l[0]
        else:
            k[i] = l[i+1]
    return k

def shift(l, n):
    t = l + []
    if n >= 0:
        for j in range(n):
            t = verplaatsingrechts(t)
    else:
        for w in range(n):
            t = verplaatsinglinks(t)
    return t
    