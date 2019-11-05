def substring(s, frm, ln):
    if ln == 0:
        return s[frm]
    else:
        for i in range(frm, frm+ln):
            x = print(s[i], end="")
        return str(x)