def lucky_numbers(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    L2=[]
    for i in range(len(l)):
        if (i-1)%2==0:
            L2.append(l[i-1])
    Ln = []
    vorige = L2[:]
    teller = 3
    for i in range(len(vorige)):
        if (i-1)%teller == 0:
            Ln.append(vorige[i-1])
    vorige = Ln[:]
    Ln = []
    return vorige
