def shift(l, n):
    li = []
    for i in range(len(l)):
        if(i+n-1 < len(l)):
            li.append(l[i+n-1])
        else:
            li.append(l[i+n-1-len(l)])
    return li