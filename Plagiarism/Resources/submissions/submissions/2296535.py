def shift(l, n):
    newlist = []
    if n > 0:
        for i in range(len(l)):
            if i+n < len(l):
                newlist.append(l[i+n+1])
            else:
                newlist.append(l[i+n-len(l)+1])
    if n < 0:
        for i in range(len(l)):
            if i+n > 0:
                list.append(l[i+n+1])
            else:
                newlist.append(l[i+n+len(l)+1])
    if i == 0: 
        return l
    return newlist