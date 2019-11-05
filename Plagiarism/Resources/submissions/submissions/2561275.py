def is_ordered(l):
    for i in range(len(l)):
        if i==0:
            if l[i]<l[i+1]:
                continue
            else:
                return False


        if i==len(l)-1:
            if l[i]>l[i-1]:
                continue
            else:
                return False
        else:
            if l[i]<l[i+1] and l[i]>l[i-1]:
                continue
            else:
                return False

    return True

    