def is_ordered(l):
    for i in range(len(l)):
        if len(l)==1:
            return True
        elif i==0:
            if l[i]<=l[i+1]:
                continue
            elif l[i]>l[i+1]:
                return False


        elif i==len(l)-1:
            if l[i]>=l[i-1]:
                continue
            elif l[i]<l[i-1]:
                return False
        elif i!=len(l)-1 and i!=0:
            if l[i]<=l[i+1] and l[i]>=l[i-1]:
                continue
            elif l[i]>l[i+1] or l[i]<l[i-1]:
                return False

    return True


    