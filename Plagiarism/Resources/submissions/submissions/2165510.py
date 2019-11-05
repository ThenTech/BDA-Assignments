def substring(s, frm, ln):
    x = ""
    for i in range(frm, frm+ln):
        x = x + s[i]
    return x

def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)+1):
        y = substring(corpus,i,len(term))
        if y == term:
            return i

def in_string(term, corpus):
    if find_pos(term,corpus) < len(corpus):
        return True