def substring(s, frm, ln):
    x = ""
    for i in range(frm, frm+ln):
        x = x + s[i]
    return x