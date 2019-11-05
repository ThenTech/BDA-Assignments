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
            else:
                continue

def in_string(term, corpus):
    if find_pos(term,corpus)!=None
        return True
    else:
        return False