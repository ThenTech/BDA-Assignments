def substring(s, frm, ln):
    woord = s
    uitkomst = woord[frm:ln+frm]
    return uitkomst

print(substring("a very long string", 3, 5))

def find_pos(term, corpus):
    for i in range(len(corpus)):
        if term == substring(corpus, i, (len(term))):
            return i
        elif i == len(corpus):
            return None
        else:
            continue

print(x)

def in_string(term, corpus):
    if find_pos(term,corpus) == (x):
        return True
    else:
        return False

