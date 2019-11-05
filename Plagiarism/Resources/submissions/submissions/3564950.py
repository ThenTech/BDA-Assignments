def substring(s, frm, len):
    result = ""
    for i in range(frm, frm + len):
        result += s[i]
    return result


def find_pos(term, corpus):
    for i in range(len(corpus)):
        sub = substring(corpus, i, len(term))
        if sub == term:
            return i

def in_string(term, corpus):
    pass