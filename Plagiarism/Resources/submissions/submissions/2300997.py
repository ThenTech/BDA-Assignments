def shift(l, n):
#    print(l)
    l.insert(0, len(l) - 1)
 #   print(l)
    del l[len(l)-1]
#    print(l)
    l.insert(1, (len(l)))
#    print(l)
    del l[len(l)-1]
#    print(l)
    return l


print(shift([1, 2, 3, 4, 5], 2))
