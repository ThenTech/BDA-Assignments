def substring(s, frm, ln):
    output = ""
    for i in range(frm, frm + ln):
        output += s[i]
    return output

def find_pos(term, corpus):
    for i in range(0, len(corpus) - len(term) + 1):
        if substring(corpus, i, len(term)) == term:
            return i


def in_string(term, corpus):
    return find_pos(term, corpus) != None