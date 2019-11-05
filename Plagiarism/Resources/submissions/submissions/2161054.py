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
x = find_pos("en", "a sententce with words")
print(x)

def in_string(term, corpus):
    y = find_pos(term, corpus)
    if find_pos(term,corpus) == int(y):
        return True
    else:
        return False

print(in_string("en", "a sententce with words"))