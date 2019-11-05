def substring(s, frm, ln):
    return s[frm:(ln+frm)]


def find_pos(term, corpus):
    index = 0

    if term in corpus:
        c = term[0]
        for ch in corpus:
            if ch == c:
                if corpus[index:index + len(term)] == term:
                    return index

            index += 1


def in_string(term, corpus):
    return bool(term in corpus)


print(substring("a very long string", 3, 5))
print(find_pos("with", "a sentence with words"))
print(in_string("with", "a sentence with words"))
