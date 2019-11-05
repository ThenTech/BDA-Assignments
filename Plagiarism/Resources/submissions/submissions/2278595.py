def substring(string, frm, len):
    respuesta = ""
    for i in range(frm, frm + len):
        respuesta = respuesta + string[i]
    return respuesta


def find_pos(term, corpus):
    total = len(corpus) - len(term) + 1;
    for i in range(0, total):
        sub = substring(corpus, i, len(term))
        if (term == sub):
            return i


def in_string(term, corpus):
    return find_pos(term, corpus) != None


print(substring("a very long string", 3, 5))
print(find_pos("with", "a sentence with words"))
print(in_string("with", "a sentence with words"))
print(find_pos("without", "a sentence with words"))
print(in_string("without", "a sentence with words"))

