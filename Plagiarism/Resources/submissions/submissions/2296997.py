def shift(l, n):
    if n > 0:
       l2 = l[len(l)-n:]
       l3 = l[:len(l)-n]
       print(l2+l3)
    elif n < 0:
       n*=-1
       l2 = l[:n]
       l3 = l[n:]
       print(l3+l2)
    else: 
       print(l)