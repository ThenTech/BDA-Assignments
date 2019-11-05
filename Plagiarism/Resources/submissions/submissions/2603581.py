def encode(s, n):
    string = ""
    for i in range(len(s)):
        if s[i] == " ":
            string += " "
        elif not("a" <= s[i] <= "z" or "A" <= s[i] <= "Z" ):
            string += s[i]
            
        else:
            string += chr((ord(s[i]) + n - 97)%26+97)
    return string


def decode(s, n):
    string = ""
    for i in range(len(s)):
        if s[i] == " ":
            string += " "
        elif not("a" <= s[i] <= "z" or "A" <= s[i] <= "Z" ):
            string += s[i]
        else:
            string += chr((ord(s[i]) - n - 97)%26+97)
    return string
