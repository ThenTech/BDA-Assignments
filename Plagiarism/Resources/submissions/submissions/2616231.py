def is_palindrome_sentence(string):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    string2 = ""
    string = string.lower()
    for i in string:
        if i not in alfabet:
            continue
        else:
            string2 += i
    list = []
    for i in string2:
        list.append(i)
    list2 = list[:]
    list2.reverse()
    return list == list2