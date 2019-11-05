def cleanup_spaces(s):
    a=""
    b=""
    for i in range(len(s)):
        if i==0 and s[i]==" ":
            a+=""
        elif i!=(len(s)-1):
            if s[i]==" " and s[i+1]!=" ":
                a+=s[i]
        if s[i]!= " ":
            a += s[i]
    for i in range(len(a)):
        if i==0 and a[i]==" ":
            b+=""
        else:
            b+=a[i]
    return b
