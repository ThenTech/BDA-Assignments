def clean_list(listy):
    listy2 = []
    for i in listy:
        if i == "":
            continue
        else:
            listy2.append(i)
    return listy2

def cleanup_spaces(s):
    listy = []
    word = ""
    for i in s+" ":
        if i == " ":
            listy.append(word)
            word = ""
        else:
            word += i

    listy = clean_list(listy)
    a = ""
    for i in listy:
        a = a + i + " "
    return a[:len(a)-1]