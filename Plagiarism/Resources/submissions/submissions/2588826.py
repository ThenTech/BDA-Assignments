def shift(l, n):
    shifted = [" "]*len(l)
    for i in range(len(l)):
        shifted[(i + n) % len(l)] = l[i]
    return shifted