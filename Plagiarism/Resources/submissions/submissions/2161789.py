def substring(s, frm, ln):
    out = ""
    for k in range(frm, ln+frm):
        out = out + s[k]
    return out

def find_pos(term, corpus):
    for i in range(len(corpus)-1):
        if term[0] == corpus[i]:
            if substring(corpus, i, len(term)) == term:
                return i

            else:
                continue
    return -1

def in_string(term, corpus):
        if find_pos(term, corpus) >= 0:
            return True
        else:
            return False
