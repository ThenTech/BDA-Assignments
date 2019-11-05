def shift(l, n):
    grote_lijst = l*n
    print(grote_lijst)
    s = grote_lijst[n+1:(n+ len(l) + 1)]
    return s