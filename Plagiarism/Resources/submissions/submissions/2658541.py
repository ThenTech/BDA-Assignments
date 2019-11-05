def shift(l, n):
    return l[len(l)-(n % len(l)):] + l[:len(l)-(n % len(l))]