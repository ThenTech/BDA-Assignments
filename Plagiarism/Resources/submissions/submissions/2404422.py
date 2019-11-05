def convert(number, n = len(number),m = 0):
    if n > 0:
        global integer
        integer += int(number[n-1])*10**m
        convert(number,n-1,m+1)
        return integer
    else:
        return