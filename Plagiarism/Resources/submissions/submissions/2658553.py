def shift(l, n):
    if len(l) > 0:
        return l[len(l)-(n % len(l)):] + l[:len(l)-(n % len(l))]