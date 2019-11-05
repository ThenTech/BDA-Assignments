def substring(s, frm, ln):
    leeg = ''
    positie = frm
    for i in range(ln):
        leeg += s[positie]
        positie += 1
        if positie >= len(s-1):
            break
    return leeg

def find_pos(term, corpus):
    j = 0

    for i in range(len(corpus)):
        if substring(corpus, j, len(term)) == term:
            return j
        j += 1

    return None

def in_string(term, corpus):
    if find_pos(term, corpus) is not None:
        return True
    else:
        return False