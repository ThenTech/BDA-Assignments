def shift(l, n):
    li = l[:]
    n = -n
    while(n < 0):
        n += len(l)

    for seq in range(n):
        temp = li[0]
        for i in range(1, len(l)):
            li[i-1] = li[i]
        li[len(l)-1] = temp
    return li