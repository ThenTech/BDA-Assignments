def convert(number, n = 0,m = 0, integer=0):
    if n != len(number):
        integer = int(number[len(number)-1-n])*10**m
        integer += convert(number,n+1,m+1, integer)
        return integer
    else:
        return 0