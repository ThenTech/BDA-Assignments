def substring(s, frm, ln):
    count = 0
    output = ""
    while count < ln:
        output += s[frm + count]
        count += 1
    return output

def find_pos(term, corpus):
    for i in range(len(corpus)):
        if term[0] == corpus[i]:
            for j in range(len(term)):
                if term[j] != corpus[i + j]:
                    break
                if j == len(term) - 1:
                    return i

def in_string(term, corpus):
        for i in range(len(corpus)):
        if term[0] == corpus[i]:
            for j in range(len(term)):
                if term[j] != corpus[i + j]:
                    break
                if j == len(term) - 1:
                    return True
    return False