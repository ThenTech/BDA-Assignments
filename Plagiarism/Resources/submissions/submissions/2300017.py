def cleanup_spaces(s):
    spatie = False
    for i in range (0, len(s)-1):
        if s[i]==" ":
            if spatie == True:
                s = s[0:i] + s[i+1:len(s)+1]
            else:
                spatie = True
        elif s[i]!=" ":
            spatie = False
            