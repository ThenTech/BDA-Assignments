def is_ordered(l):
    n=-1
    for x in l[:len(l)-1]:
       n+=1
       if l[n] > l[n+1]:
           print(False)
           break
    print (True)