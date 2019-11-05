def encode(s, n):
    string = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    n = n%len(alfabet)
    if len(s) ==0:
        return s
    for i in s:
        if i not in alfabet:
            string += i
        else:
            for j in range(len(alfabet)):
                if i == alfabet[j]:
                    string += alfabet[j+n]
                    break
    return string


def decode(s, n):
    string = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    n = n%len(alfabet)
    if len(s) ==0:
        return s
    for i in s:
        if i not in alfabet:
            string += i
        else:
            for j in range(len(alfabet)):
                if i == alfabet[j]:
                    string += alfabet[j-n]
                    break
    return string