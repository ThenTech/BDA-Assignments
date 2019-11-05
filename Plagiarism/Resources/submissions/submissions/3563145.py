def substring(s, frm, ln):
    subs = ""
    for i in range(frm, frm + ln):
        if frm + ln >= len(s):
            return None
        else:
            subs += s[i]

    return subs

def find_pos(term, corpus):
    length_term = len(term)
    length_corpus = len(corpus)
    for i in range(length_corpus):
        if substring(corpus, i, length_term) == term:
            return i

def in_string(term, corpus):
    return bool(find_pos(term, corpus) != None)