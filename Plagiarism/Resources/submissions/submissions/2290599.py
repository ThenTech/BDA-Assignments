def is_ordered(l):
    for x in l:
        if l[x] > l[x-1]:
            print(False)
    print(True) 