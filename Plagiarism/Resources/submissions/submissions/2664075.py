def shift(l,n):
    copy = []
    for i in range(len(l)):
        old_i = (i-n) % len(l)
        copy.append([old_i])
    return copy