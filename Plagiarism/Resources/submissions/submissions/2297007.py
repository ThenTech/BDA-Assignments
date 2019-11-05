def lucky_numbers(n):
    l = [x+1 for x in range(n)]
    for x in range(len(l)):
        y = x+2
        while y<len(l[:]):
            l.remove(y)
            y += y
    return(l)