def lucky_numbers(n):
    l = [x+1 for x in range(n)]
    for x in range(l):
        for y in range(floor(len(l)/(x+2))):
            l.remove((y+1)*(x+2))
    return(l)