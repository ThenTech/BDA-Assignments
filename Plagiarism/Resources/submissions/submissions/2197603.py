import string


def count_words(s):
    output = ""
    numbers = "1234567890"
    for letter in s:
        if letter in string.punctuation:
            s = s.replace(letter, "")
    for letter in s:
        if letter in numbers:
            s = s.replace(letter, "")
    s = s.lower()
    s = s.replace(" ", "")
    for i in range(len(s)):
        backwards = s[len(s) - 1 - i]
        output += backwards
    if output == s:
        return True
    else:
        return False