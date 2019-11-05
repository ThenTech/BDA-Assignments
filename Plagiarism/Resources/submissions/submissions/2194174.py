import math
import string
alfabet="abcdefghijklmnopqrstuvwxyz"
def find(s, ch):
    x = 0
    while x < len(s):
        if s[x] == ch:
            return x
        x += 1
    return -1
def encode(s,n):
    if n < 0:
        n=n + 26*abs(math.floor(n/26))
    elif n > 25:
        n = n - 26*math.floor(n/26)
    for p in s:
        if p == " ":
            print(" ", end="")
        elif p in string.punctuation:
            print(p, end="")
        else:
            g = find(alfabet, p) + n
            if g > 25:
                g = g - 26
            print(alfabet[g], end="")


def decode(s, n):
    pass