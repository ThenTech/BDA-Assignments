def substring(s, frm, ln):
    output = ""
    for k in range(frm, ln+frm):
        output = output + s[k]
    return output

def find_pos(term, corpus):
    for i in range(len(corpus)-1):
        if term[0]==corpus[i]:
            if substring(corpus, i, len(term))== term:
                return i
            elif i==len(corpus):
                return None
            else:
                continue

def in_string(term, corpus):
    for i in range(len(corpus)+1):
        if term[0]==corpus[i]:
            if substring(corpus, i, len(term))== term:
                return True
            else:
                continue
        return False