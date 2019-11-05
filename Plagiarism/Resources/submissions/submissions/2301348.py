def lucky_numbers(n):
    l = []
    for i in range(1,n+1):
        l += [i]
    teller = n
    for j in range(1, n+1):
        if teller == teller-teller//j:
            return l
        else:
            for k in range(teller//j):
                del l[j-1+k*j]
        teller = teller-teller//j