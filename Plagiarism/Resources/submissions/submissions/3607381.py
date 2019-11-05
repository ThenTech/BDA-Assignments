def shift(l, n):
    while n < len(l):
        n += len(l)
    while n >= len(l):
        n -= len(l)
        
    output = []
    for i in range(len(l)):
        if n + i >= len(l):
            n -= len(l)
        output.append(l[i+n])
    return output;