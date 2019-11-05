def shift(l, n):
    if l == "":
        return
    
    while n < len(l):
        n += len(l)
    while n >= len(l):
        n -= len(l)
        
    output = []
    for i in range(1, len(l)+1):
        if n + i >= len(l):
            n -= len(l)
        output.append(l[i+n])
    return output