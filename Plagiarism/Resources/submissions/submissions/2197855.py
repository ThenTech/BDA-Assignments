def replace(pattern, replacement, corpus):
    s = s.split()
    s_a = ''
    for i in s:
        if w not in i:
            s_a += i + ' '
        else:
            s_a += (f + i[len(w):])+' '
    return s_a