import math

letters = "abcdefghijklmnopqrstuvwxyz"
def encode(s, n):
    newword = ""
    x = abs(n) // 26
    for i in range(len(s)):
        if s[i] not in letters:
            newword += s[i]
        elif ord(s[i]) + n > ord("z"):
            newword += chr(ord(s[i]) - 26 + (x+1)*n)
        elif ord(s[i]) + n < ord("a"):
            newword += chr(ord(s[i]) + 26 + (x+1)*n)
        else:
            newword += chr(ord(s[i]) + n)
    return newword

def decode(s,n):
    newword = ""
    for i in range(len(s)):
        if s[i] not in letters:
            newword += s[i]
        elif ord(s[i]) - n > ord("z"):
            newword += chr(ord(s[i]) - 26 - n)
        elif ord(s[i]) - n < ord("a"):
            newword += chr(ord(s[i]) + 26 + n)
        else:
            newword += chr(ord(s[i]) - n)
    return newword


