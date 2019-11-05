def shift(l, n):
    x = len(l)-1
    y = []
    con = []

    if n >= 0:
        for i in range(n):
            con.append(n-i)

        for i in con:
            y.append(l[len(l)-i])
    
        for i in range(len(l)-n):
            y.append(l[i])

    else:
        n = n * -1
        
        for i in range(n):
            con.append(i+1)

        for i in range(n+1):
            y.append(l[i+n])

        for i in range(n):
            y.append(l[i])

    return y