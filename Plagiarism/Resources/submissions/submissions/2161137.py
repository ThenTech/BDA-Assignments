def substring(s, frm, ln):
    leeg = "'"
    positie = frm
    for i in range(ln):
        leeg += s[positie]
        positie += 1

    print(leeg, end="'")
    print()
    pass

substring("a very long string", 3, 5)

def find_pos(term, corpus):
    i = 0
    j = 0
    while term[i] != corpus[j]:
        j += 1
    x = j
    while i < len(term) and term[i] == corpus[x]:
        x += 1
        i += 1
    if len(term) == x - j:
        print(j)
    else:
        print("")
    pass

find_pos("with", "a sentence with words")

def in_string(term, corpus):
    i = 0
    j = 0
    while term[i] != corpus[j]:
        j += 1
    x = j
    while i < len(term) and term[i] == corpus[x]:
        x += 1
        i += 1
    return len(term) == x - j
    pass

in_string("with", "a sentence with words")