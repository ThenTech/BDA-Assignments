s = input("geef een woord of zin: ")
frm = int(input("vanaf welke plaats: "))
ln = int(input("hoe lang: "))
def substring(s, frm, ln):
    output = ""
    for i in range(frm, ln+frm):
        output += s[i]
        return output
substring(s, frm, ln)


term = input("geef het woord dat je zoekt: ")
corpus = input("geef de zin waar in je zoekt: ")
def find_pos(term, corpus):
    for j in range (len(corpus)-len(term)):
         if term[0] == corpus [j]:
             if substring(corpus, j, len(term)):
                 return j  
find_pos(term, corpus)

def in_string(term, corpus):
    def find_pos(term, corpus):
        for l in range (len(corpus)-len(term)):
            if term[0] == corpus [l]:
                if substring(corpus, l, len(term)):
                    return l
                
