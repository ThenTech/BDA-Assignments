def merge_lists(f, s):
    Result = []
    p = len(f) + len(s)
    for i in range(0, p):
        if len(f) > 0 and len(s) > 0:
            if f[0] < s[0]:
                Result.append(f[0])
                f = f[1:]

            else:
                Result.append(s[0])
                s = s[1:]
        else:
            if len(f) == 0:
                for i in range(len(s)):
                    Result.append(s[i])
                    
            else:
                for i in range(len(f)):
                    Result.append(f[i])
            break
    return Result

####################################################
def merge_sort(l):
    z = ""
    q = ""
    k = ""
    if len(l) <= 1:
        return l
    else:
        div = len(l) // 2
        print(l[0:div], l[div:])
        
        
        if len(l[0:div]) > 1:
            z = merge_sort(l[0:div])
        elif len(l[0:div]) == 1:
            z = l[0:div]
        if len(l[div:]) > 1:
            q = merge_sort(l[div:])
        elif len(l[div:]) == 1: 
            q = l[div:]
        
        #print(merge_lists(l[0:div], l[div:]))
        k =  merge_lists(z, q)
        return k