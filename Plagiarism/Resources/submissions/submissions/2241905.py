def encode(s, n):
    string = ""
    for i in s:
        if 'a' <= i <= (chr(ord('z') - (n % 26))) or 'A' <= i <= (chr(ord('A') - (n % 26))):
            string = string + chr(ord(i) + (n % 26))
        elif chr(ord('z') - (n % 26) + 1) <= i <= 'z' or chr(ord('Z') - (n % 26) + 1) <= i <= 'Z':
            string = string + chr(ord(i) - (26 - (n % 26)))
        else:
            string = string + i
    return string

def decode(s, n):
    return encode(s,(-1)*n)