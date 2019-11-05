def shift(l, n):
    n = int(n)
    l2 = []
    for i in range(0,len(l)):   # 0,5
        l2.append(l[(i+(len(l)-n))%len(l)])     #0.4+2%6
    return l2