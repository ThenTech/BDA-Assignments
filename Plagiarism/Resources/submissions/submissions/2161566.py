def substring(s, frm, ln):
    for k in range(ln):
        print(s[frm+k], end="")
def find_pos(term, corpus):
    juist = False
    for l in range(len(term)):
        for m in range(len(corpus)):
            if term[l] == corpus[m]:
                if term == corpus[m: m+len(term)]:
                    juist = True
                    start=m
                    break
    if juist == True:
        print(start)
    else:
        print(None)
def in_string(term, corpus):
    juist = False
    for l in range(len(term)):
        for m in range(len(corpus)):
            if term[l] == corpus[m]:
                if term == corpus[m: m + len(term)]:
                    juist = True
                    start = m
                    break
    if juist == True:
        print(True)
    else:
        print(False)
