def shift(l, n):
    while n > len(l):
        n = n - len(l)
    if l == []:
        return l
    if n > 0:
        return l[n:] + l[:n]
    elif n < 0:
        return l[n-1:] + l[:n-1]
    else:
        return l
print(shift([], 9))