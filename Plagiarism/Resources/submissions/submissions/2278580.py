def substring(s, frm, ln):
    respueta= ''
    for letra in range(frm, frm+len(ln)):
        respuesta= respuesta + s[i]
        return respuesta



def find_pos(term, corpus):
    
    total= len(corpus)- len(term)+1
    for i in range(0, total):
        parte= substring(corpus, i, len(term))
        if parte==term:
            return i
            




    if find_pos(term, corpus) is True:
        return True


print(substring("a very long string", 3, 5))
print(find_pos("with", "a sentence with words"))
print(in_string("with", "a sentence with words"))
print(find_pos("without", "a sentence with words"))
print(in_string("without", "a sentence with words"))
