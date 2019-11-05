def substring(s, frm, ln):
    uitvoer = ""
    for i in range(frm, frm+ln):
        uitvoer += s[i]
    return uitvoer

def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)+1):
        woordzoeken = substring(corpus, i, len(term))
        if term == woordzoeken:
            return i
def in_string(term, corpus):
    return find_pos(term, corpus) != None


