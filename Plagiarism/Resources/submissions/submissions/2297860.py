def lucky_numbers(n):
    s = []
    t = []
    n = int(n)
    for i in range(1, n+1):
        s.append(i)

    for q in range(2, len(s)): # getallen
        if q < len(s):
            for z in range(1, len(s)+1): # elementen
                if z % q != 0:
                    t.append(s[z-1])
            s = t[:]
            t = []
        else:
            break
        return s