def encode(s, n):
    string = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i not in alfabet:
            string += i
        else:
            for j in range(len(alfabet)):
                if i == alfabet[j]:
                    string += alfabet[j+n]


def decode(s, n):
    string = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i not in alfabet:
            string += i
        else:
            for j in range(len(alfabet)):
                if i == alfabet[j]:
                    string += alfabet[j-n]