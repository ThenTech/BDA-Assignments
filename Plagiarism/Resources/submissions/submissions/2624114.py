def substring(s, frm, ln):
    lijst = []
    for letter in s:
        lijst.append(letter)
        index = -1
        uitkomst = ''
    for teken in lijst:
        index += 1
        if frm <= index < frm+ln:
            uitkomst += teken
    return uitkomst
        

def find_pos(term, corpus):
    pass

def in_string(term, corpus):
    pass