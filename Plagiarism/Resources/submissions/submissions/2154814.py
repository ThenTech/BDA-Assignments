def substring(s, frm, ln):
    sub = ""
    for i in range(frm, frm+ln):
        sub += s[i]
    return sub

def find_pos(term, corpus):
    first_term_letter = term[0]
    corpus_index = 0
    for letter in corpus:
        if letter == first_term_letter:
            return corpus_index
        index += 1

def in_string(term, corpus):
    i = 0
    corpus_index = 0
    first_term_letter = term[0]

    for letter in corpus:
        if corpus_index == len(corpus) - len(term) + 1:
            return False

        if letter == first_term_letter:
            for x in range(corpus_index, corpus_index + len(term)):
                if corpus[x] == term[i]:
                    i += 1
                    x += 1
                    if i == len(term) - 1:
                        return True
                else:
                    i = 0
        corpus_index += 1