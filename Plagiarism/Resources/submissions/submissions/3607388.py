def shift(l, n):
    if l == "":
        return
    
    while n < len(l):
        n += len(l)
    while n >= len(l):
        n -= len(l)
        
    output = []
    for i in range(len(l)):
        if n + i >= len(l):
            n -= len(l)
        output.append(l[i+n+1])
    return output