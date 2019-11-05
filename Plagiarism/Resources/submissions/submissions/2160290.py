def substring(s, frm, ln):
    for i in range(frm, frm+ln):
        print(s[i], end="")

def find_pos(term, corpus):
    count = 0
    for i in range(0, len(corpus)):
        if corpus[i] == term[0]:
            for j in range(i, i + len(term) - 1):
                start = j
                if corpus[j] == term[count]:
                    count += 1
                else:
                    pass
    if count == len(term) - 1:
        return start
    else:
        return None
   
def in_string(term, corpus):
    count = 0
    for i in range(0, len(corpus)):
        if corpus[i] == term[0]:
            for j in range(i, i + len(term) - 1):
                start = j
                if corpus[j] == term[count]:
                    count += 1
                else:
                    pass
    if count == len(term) - 1:
        return True
    else:
        return None


s = input("Geef een string in : ")
frm = int(input("Geef de begin index op : "))
ln = int(input("Geef aan hoeveel karakters je hierbij wilt bijtellen : "))

substring(s, frm, ln)
term1 = input("geef een string op : ")
corpus1 = input("geef een zin op : ")
test = find_pos(term1, corpus1)
print(test)