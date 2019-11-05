lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_lower(letter):
    for i in range(len(upper)):
        if upper[i] == letter:
            return lower[i]


def is_palindrome_sentence(sentence):
    letters = ""
    for c in sentence:
        if "a" <= c <= "z":
            letters += c
        if "A" <= c <= "Z":
            letters += get_lower(c)
    for i in range(len(letters)):
        if letters[i] != letters[len(letters)-1-i]:
            return False
    return True