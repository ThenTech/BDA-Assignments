def lucky_numbers(n):
    l = [x+1 for x in range(n)]
    for x in range(len(l)):
        for y in range(round(len(l)/(x+2))):
            l.remove((y+1)*(x+2))
    return(l)