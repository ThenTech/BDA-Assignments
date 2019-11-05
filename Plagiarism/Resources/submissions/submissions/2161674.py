def substring(s, frm, ln):
    for i in range(ln):
        print(s[frm+i], end="")

def find_pos(term, corpus):
    juist = False
    for i in range(len(term)):
        for k in range(len(corpus)):
            if str(term[i]) == str(corpus[k]):
                if str(term == corpus(k + len(term))):
                    juist = True
                    return k


def in_string(term, corpus):
    for i in range(len(term)):
        for k in range(len(corpus)):
            if str(term[i]) == str(corpus[k]):
                for x in range(len(term)):
                    if term[i + x] == corpus[k + x]:
                        return True
                    else:
                        return False

