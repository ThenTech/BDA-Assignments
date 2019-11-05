def cleanup_spaces(s):
    spatie = False
    if s[0]==" ":
        s = s[1:len(s)-1]
        spatie = True
    for i in range (0, len(s)-1):
        if i>= len(s)-1:
            if s[i]==" ":
                s = s[0:i]
            break
        if s[i]==" ":
            if spatie == True:
                s = s[0:i] + s[i+1:len(s)+1]
            else:
                spatie = True
        elif s[i]!=" ":
            spatie = False
    return s        