def cleanup_spaces(s):
    spatie = False
    while s[0]==" ":
        if len(s)==1:
            s=""
            break
        s = s[1:len(s)+1]
        
    for i in range (0, len(s)-1):
        if i>= len(s)-1:
            if s[i]==" ":
                s = s[0:i]
            break
        if s[i]==" ":
            if spatie == True:
                s = s[0:i] + s[i+1:len(s)+1]
                i-=1
            else:
                spatie = True
        elif s[i]!=" ":
            spatie = False
    return s        