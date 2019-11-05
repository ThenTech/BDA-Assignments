def substring(s, frm, ln):
    sub = ""
    for i in range(frm, frm + ln):
        letter = s[i]
        sub = sub + letter
    return sub

def find_pos(term, corpus):
    for j in range(0, len(corpus) - len(term) + 1):
        part = substring(corpus, j, len(term))
        if part in term:
            return j

def in_string(term, corpus):
    found = find_pos(term, corpus)
    if found == None:
        return False
    else:
        return True