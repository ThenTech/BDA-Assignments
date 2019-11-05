import string


def to_lowercase(sentence):
    newsentence = ""

    for char in sentence:
        if "A" <= char <= "Z":
            ordinal = ord(char) - ord("A")
            newsentence += chr(ord("a") + ordinal)
        else:
            newsentence += char
    return newsentence


def strip_special_tokens(sentence):
    newsentence = ""

    for char in sentence:
        if char not in string.punctuation:
            newsentence += char
        else:
            newsentence += ""
    return newsentence


def delete_spaces(sentence):
    newsentence = ""

    for char in sentence:
        if char == " ":
            newsentence += ""
        else:
            newsentence += char
    return newsentence


def is_palindrome_sentence(sentence):
    newsentence = to_lowercase(sentence)
    newsentence = strip_special_tokens(newsentence)
    newsentence = delete_spaces(newsentence)

    for i in range(0, len(newsentence)//2):
        if newsentence[i] != newsentence[len(newsentence) - i - 1]:
            return False
    return True
