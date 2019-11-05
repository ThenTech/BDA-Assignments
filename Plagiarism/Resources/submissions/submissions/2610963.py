def substring(s, frm, ln):
    result = ""
    for i in range(ln):
        result += s[frm+i]
    return result


def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)+1):
        if term == substring(corpus, i, len(term)):
            return i


def in_string(term, corpus):
    if term in corpus:
        return True
    return False


substring("a very long string", 3, 5)
find_pos("with", "a sentence with words")
in_string("with", "a sentence with words")
