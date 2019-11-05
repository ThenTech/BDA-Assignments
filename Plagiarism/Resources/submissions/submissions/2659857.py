def substring(s, frm, ln):
    stuk = ""
    for getal in range(frm, frm + ln):
        stuk += s[getal]
    return stuk

def find_pos(term, corpus):
    if term not in corpus:
        return None
    else:
        for i in range(len(corpus)-len(term)+1):
            if substring(corpus, i, len(term)) == term:
                return i

def in_string(term, corpus):
    if term in corpus:
        return True
    else:
        return False