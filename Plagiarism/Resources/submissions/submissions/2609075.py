def shift(l, n):
    copy = []
    for i in range(len(l)):
        new = (i-n) % len(l)
        copy.append(lijst[new])
    return copy