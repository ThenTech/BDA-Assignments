def is_ordered(l):
    for x in l[:len(l)-1]:
        if l[x] > l[x-1]:
            print(False)
    print(True) 