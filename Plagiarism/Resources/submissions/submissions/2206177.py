def replace(s1, s2, s3):
    newstring = ""
    i = 0
    while i < len(s3):
        if s3[i:i+len(s1)] == s1:
            newstring += s2
            i += len(s1)
        else:
            newstring += s3[i]
            i += 1
    return newstring