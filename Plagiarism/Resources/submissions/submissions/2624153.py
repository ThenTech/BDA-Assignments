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
    if find_pos(term,corpus) == None:
        return False
    else:
        return True

print(in_string("neee", "a sententce with words"))