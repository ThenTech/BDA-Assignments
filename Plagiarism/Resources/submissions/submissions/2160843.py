def substring(s, frm, ln):
    output = ""
    for k in range(frm, ln+frm):
        output = output + s[k]
    return output
    pass

def find_pos(term, corpus):
    for i in range(len(corpus)+1):
        if term[0]==corpus[i]:
            if substring(corpus, i, len(term))== term:
                return i
            else:
                continue
        return None

def in_string(term, corpus):
    for i in range(len(corpus)+1):
        if term[0]==corpus[i]:
            if substring(corpus, i, len(term))== term:
                return True
            else:
                continue
        return False