l=input()
def is_ordered(l):
    for x in l-1:
        if l[x] > l[x-1]:
            print(False)
    print(True) 
