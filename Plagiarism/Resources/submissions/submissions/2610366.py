def cleanup_spaces(s):
    spatie = " "
    a=0
    for i in range(len(s)-1):
        if s[len(s)-1-i] == spatie:
            s= s[:i]
        else:
            break
        break
    for i in range(len(s)-1):
        if s[i] != spatie:
            a+=1
        if a <1 and s[i] == spatie:
            s= s[:i]+s[i+1:]
        elif s[i] == spatie and s[i-1]== spatie:
            s = s[:i]+s[i+1:]
    return s
            