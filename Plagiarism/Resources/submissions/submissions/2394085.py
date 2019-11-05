def cleanup_spaces(s):
    n = ""
    for i in range(1,len(s)-1):
        k=functie (i,s)
        if k != None:
           n +=k
        if i ==len(s)+1:
            return n
def functie(i,s):
    if i==1 and s[i]!=" ":
        return s[i]
    elif i==len(s)-1 and s[i] != " ":
        return s[i]
    elif  s[i] != " ":
        return s[i]
    elif s[i+1] !=" " and s[i]==" ":
        return s[i]