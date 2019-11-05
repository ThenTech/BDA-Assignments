def remove_punc(sentence):
    inword = True
    sans_punc = ""
    for i in sentence:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            sans_punc += i
    return remove_upper(sans_punc)

def remove_upper(sans_punc):
    sans_upper = ""
    for i in sans_punc:
        if "A" <= i <= "Z":
            result = chr(ord(i) - ord("A") + ord("a"))
            sans_upper += result
        else:
            sans_upper += i
    return is_palindrome_sentence(sans_upper)


def is_palindrome_sentence(sans_upper):
    palin = True
    for i in range(len(sans_upper)):
        palin = sans_upper[i] == sans_upper[len(sans_upper) - i - 1]
        if palin:
            i += 1
        else:
            return palin
    return palin