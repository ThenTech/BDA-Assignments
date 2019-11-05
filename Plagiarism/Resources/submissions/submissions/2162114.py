def substring(s, frm, ln):
    string = ""
    c = 0
    while c < int(ln):
        letter = s[int(frm+c)]
        string += letter
        c += 1
    return string

def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)+1):
        if term == substring(corpus, i, len(term)):
            return int(i)

def in_string(term, corpus):
    if type(find_pos(term, corpus)) == int:
        return True
    else:
        return False