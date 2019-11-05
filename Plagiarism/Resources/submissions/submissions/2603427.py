e = input("")
d = input("")

def encode(s, n):
    string = ""
    for i in range(len(s)):
        if s[i] == " ":
            string += " "
        else:
            string += chr((ord(s[i]) + n - 97)%26+97)
    print(string)


def decode(s, n):
    string = ""
    for i in range(len(s)):
        if s[i] == " ":
            string += " "
        else:
            string += chr((ord(s[i]) - n - 97)%26+97)
    print(string)

decode(d, n)
encode(e, n)