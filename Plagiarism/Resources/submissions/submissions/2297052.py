def lucky_numbers(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    Ln = []
    vorige = l[:]
    teller = 2
    j = 0
    while j < n/2:
        for i in range(len(vorige)):
          if (i+1)%teller != 0:
             Ln.append(vorige[i])
        vorige = Ln[:]
        Ln = []
        j += 1
        teller +=1
    return vorige