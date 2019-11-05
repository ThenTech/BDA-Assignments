def substring(s, frm, ln):
    newword = ""
    for i in range(frm, frm + ln):
        newword += s[i]
    return newword


def in_string(term, corpus):
    for j in range(len(corpus)-len(term)):
        newword = ""
        for i in range(j, len(term) + j):
            newword += corpus[i]
        if newword == term:
            return True
        else:
            continue
    return False
def find_pos(term, corpus):
    for j in range(len(corpus)-len(term)):
        newword = ""
        for i in range(j, len(term) + j):
            newword += corpus[i]
        if newword == term:
            pos = j + 1
            break
        else:
            continue
    print(pos)