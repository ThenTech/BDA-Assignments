alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mirror(s):
    reverse_s = ""
    for i in range(len(s)):
        reverse_s += s[len(s) - 1 - i]
    return reverse_s

def punctuation(s):
    p = ""
    for i in range(len(s)):
        if s[i] in alphabet1:
            p += s[i]
    return p

def lowercase(s):
    lower = ""
    for i in range(len(s)):
        if s[i] not in alphabet:
            letter = char(ord("a") + ord(s[i]) - ord("A"))
            lower += letter
        else:
            lower += s[i]
    return lower
    
def is_palindrome_sentence(sentence):
    new_sentence = lowercase(punctuation(sentence))
    return new_sentence == mirror(new_sentence)