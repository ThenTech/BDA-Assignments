def shift(l, n):
    lijst = l[:]
    for li in range(len(l)):
        index = (li+n)%len(l)
        lijst[index] = l[li]
    return lijst
