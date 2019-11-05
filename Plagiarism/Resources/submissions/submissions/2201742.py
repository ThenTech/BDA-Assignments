def cleanup_spaces(s):
    spatie = False
    for i in range (0, len(s)):
        if s[i]==" ":
            if spatie == True:
                s = s[0:i-1] + s[i+1:len(s)+1]
            else:
                spatie = True
        elif s[i]!=" ":
            spatie = False
            