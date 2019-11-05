def merge_lists(first,second):
    lengte = len(second)
    newlist = []
    if len(first)<=len(second):
        lengte = len(first)
    i = 0
    while i < lengte:
        if first[i] <=second[0]:
            newlist.append(first[i])
            i += 1
        else:
            newlist.append(second[0])
            second = second[1:]
            if len(second)==0:
                newlist.append(first[i:])
                break
    newlist.append(second)
    return newlist

def merge_sort(l):
    if len(l)==1:
        return l
    else:
        x = len(l)//2
        le=l[:x]
        lt=l[x:]
        u = merge_sort(le)
        v=merge_sort(lt)
        ld=merge_lists(u,v)
        return ld