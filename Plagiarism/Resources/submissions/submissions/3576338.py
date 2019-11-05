def substring(s, frm, ln):
    output = ""
    for i in range(frm, frm + ln):
        output += s[i]
    return output

def find_pos(term, corpus):
    for i in range(len(corpus)):
        if substring(corpus, i, len(term)) == term:
            return i
    return None

def in_string(term, corpus):
    if find_pos(term, corpus) == None:
        return False
    return True