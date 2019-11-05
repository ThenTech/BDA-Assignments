def substring(s, frm, ln):
    woord = s
    uitkomst = woord[frm:ln+frm]
    return uitkomst

print(substring("a very long string", 3, 5))

def find_pos(term, corpus):
    for x in range(len(corpus)):
        if term == substring(corpus, x, (len(term))):
            return x
        elif x == len(corpus):
            return None
        else:
            continue
x = find_pos("with", "a sentence with words")
print(x)

def in_string(term, corpus):
    if find_pos(term,corpus) == (x):
        return True
    else:
        return False

print(in_string("with", "a sentence with words"))