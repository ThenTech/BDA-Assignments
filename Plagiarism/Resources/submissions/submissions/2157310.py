def substring(s, frm, ln):
    return s[frm:(ln+frm)]


def find_pos(term, corpus):
    return corpus.find(term)


def in_string(term, corpus):
    return bool(term in corpus)


print(substring("a very long string", 3, 5))
print(find_pos("with", "a sentence with words"))
print(in_string("with", "a sentence with words"))
