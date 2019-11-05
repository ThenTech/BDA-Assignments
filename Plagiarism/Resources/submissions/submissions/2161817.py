def substring(s, frm, ln):
    string = ""
    c = 0
    while c < int(ln):
        letter = s[int(frm+c)]
        string += letter
        c += 1
    return string

def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)):
        if term == substring(corpus, i, len(term)):
            return i

def in_string(term, corpus):
    teller = 0
    for i in term:
        for j in corpus:
            if i == j:
                return True
            else:
                teller += 1