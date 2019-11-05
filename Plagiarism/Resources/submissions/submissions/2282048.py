def zoek(pattern, corpus):
   aantal = 0
   for teller in range(len(corpus)-len(pattern)):
       if corpus[teller:teller+len(pattern)] == pattern:
           aantal = aantal + 1
   return aantal

"""
def vervang(string,vervanging, zin):
    teller = 0
    for x in string:
        if x == " ":
            teller = teller + 1
    for x in range(teller):
        teller = 0
        start_pos = ""
        el = string[teller]
        while el != " ":
            start_pos = start_pos + el
            teller = teller + 1
        start_pos = int(start_pos)
        zin = zin[:start_pos] + vervanging + zin[start_pos+1:]
    return zin
"""




def replace(pattern, replace, corpus):
    aantal = zoek(pattern, corpus)
    for x in range(aantal):
        for teller in range(len(corpus) - len(pattern)):
            if corpus[teller:teller + len(pattern)] == pattern:
                corpus = corpus[:teller] + replace + corpus[teller+len(pattern):]
    return corpus