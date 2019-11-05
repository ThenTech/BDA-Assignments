def shift(l, n):
    x = ["h"]*len(l)
    for i in range(n,len(l)+n):
        x[i%(len(l))] = l[i-n]
    return x
