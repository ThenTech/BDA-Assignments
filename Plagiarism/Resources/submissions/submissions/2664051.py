def substring(string, frm, len):
    result = ""
    for i in range(frm, frm + len):
        result = result + string[i]
    return result


def find_pos(term, corpus, start):
    end = len(corpus) - len(term) + 1;
    for i in range(start, end):
        sub = substring(corpus, i, len(term))
        if (term == sub):
            return i
    return len(corpus)


def replace(pattern, replacement, corpus):
    output = ""
    i = 0
    while (i < len(corpus)):
        start_pat = find_pos(pattern, corpus, i)
        output += substring(corpus, i, start_pat - i)
        if (start_pat != len(corpus)):
            output += replacement
        i = start_pat + len(pattern)
    return output