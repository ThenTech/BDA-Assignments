def substring(s, frm, ln):
    max = frm + ln
    string = s [frm: max]
    return string
    
def find_pos(term, corpus):
    a = len(term)
    for x in range(len(corpus)-len(term)+1):

        if corpus[x:x+a] == term:
            return x


def in_string(term, corpus):
    if term in corpus:
        return True
    else:
        return False