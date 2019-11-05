def shift(l, n):
#    print(l)
    l.insert(0, len(l))
 #   print(l)
    del l[len(l)-1]
#    print(l)
    l.insert(1, (len(l)-1))
#    print(l)
    del l[len(l)-1]
#    print(l)


