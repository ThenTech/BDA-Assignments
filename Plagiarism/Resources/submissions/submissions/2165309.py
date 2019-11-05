def substring(s, frm, ln):
    if ln == 0:
        return s[frm]
    else:
        x = ""
        for i in range(frm, frm+ln):
            x = x + s[i]
        return x