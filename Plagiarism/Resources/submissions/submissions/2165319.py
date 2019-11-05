def substring(s, frm, ln):
    if ln == 0:
        y =""
        y = s[frm]
        return y
    else:
        x = ""
        for i in range(frm, frm+ln):
            x = x + s[i]
        return x