def shift(l,n):
    new_list = []
    for i in l:
        if (i-n)%len(l) == 0:
            new_list.append(len(l))
        else: 
            new = (i-n)%len(l)
            new_list.append(new)
    return new_list

