alfabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def find(s, ch):
    x = 0
    while x < len(s):
        if s[x] == ch:
            return x
        x += 1
    return -1

def encode(s, n):
    uitkomst =''
    for letter in s:
        if letter in alfabet:
            positieinalfabet = find(alfabet, letter)
            nieuwepositieinalfabet = positieinalfabet+n
            letter = alfabet[nieuwepositieinalfabet]
            uitkomst += letter
        else:
            uitkomst += letter
    return uitkomst
encode("sean", 5)


def decode(s, n):
    uitkomst = ''
    for letter in s:
        if letter in alfabet:
            positieinalfabet = find(alfabet, letter)
            nieuwepositieinalfabet = positieinalfabet - n +1
            letter = alfabet[nieuwepositieinalfabet]
            uitkomst += letter
        else:
            uitkomst += letter
    return uitkomst

print(decode("gcp", 3))