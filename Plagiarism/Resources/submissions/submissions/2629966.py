def encode(s, n):
    string = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    if len(string) ==0:
        return string
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
    if len(string) ==0:
        return string
    for i in s:
        if i not in alfabet:
            string += i
        else:
            for j in range(len(alfabet)):
                if i == alfabet[j]:
                    string += alfabet[j-n]
                    break
    return string