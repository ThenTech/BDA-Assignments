def shift(l, n):
    inputlist = l[:]
    shifted_list = []
    n = int(n)
    x = 0
    print(inputlist)
    toobig = False

    for i in range(0, len(inputlist)):
        x = i + n
        if x >= len(inputlist):
            toobig == True
        while toobig:
            x -= len(inputlist)
            if x < len(inputlist):
                toobig == False
        shifted_list[x:x+1] = [inputlist[i]]
        return shifted_list