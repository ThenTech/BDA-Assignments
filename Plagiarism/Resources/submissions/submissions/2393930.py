def cleanup_spaces(s):

    for i in range(1,len(s)-1):
        k=functie (i,s)
        if k != None:
            print(k,end="")
def functie(i,s):
    if  s[i] != " ":
        return s[i]
    elif s[i-1] != " " and s[i+1] !=" " and s[i]==" ":
        return s[i]