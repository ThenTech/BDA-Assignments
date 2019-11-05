def substring(s, frm, ln):
    print(s[frm:(ln+frm)])


def find_pos(term, corpus):
    print(corpus.find(term))


def in_string(term, corpus):
    if term in corpus:
        return True
    else:
        return False