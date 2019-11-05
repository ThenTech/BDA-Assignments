def substring(s, frm, ln):
    return s[frm:(ln+frm)]

def find_pos(term, corpus):
    found = None
    for i in range(len(corpus)-len(term)):
        if substring(corpus, i, len(term)) == term:
            found = i
    return found

def in_string(term, corpus):
    return find_pos(term, corpus)!=None