def substring(s, frm, ln):
    sub = ""
    for i in range(frm, frm+ln):
        sub += s[i]
    return sub

def find_pos(term, corpus):
    for i in range(0, len(corpus)):
        counter = 0
        for y in range(0, len(term)):
            if i+y < len(corpus):
                if term[y] == corpus[i+y]:
                    counter +=1
                else :
                    break
            else:
                break
        if (counter == len(term)):
            return  i
            break

def in_string(term, corpus):
    result = False
    for i in range(0, len(corpus)):
        counter = 0
        for y in range(0, len(term)):
            if i+y < len(corpus):
                if term[y] == corpus[i+y]:
                    counter +=1
                else :
                    break
            else:
                break
        if (counter == len(term)):
            result = True
            break
    return result


substring("a very long string", 3, 5)
find_pos("with", "a sentence with words")
in_string("abc", "a sentence with words")
