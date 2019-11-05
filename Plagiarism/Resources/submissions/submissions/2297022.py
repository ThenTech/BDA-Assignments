def shift(l, n):
    if n > 0:
       if n > len(l):
           n -= len(l)
       l2 = l[len(l)-n:]
       l3 = l[:len(l)-n]
       return l2+l3
    elif n < 0:
       n *= -1
       l2 = l[:n]
       l3 = l[n:]
       return l3+l2
    else: 
       return l