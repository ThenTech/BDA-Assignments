import string


def is_palindrome_sentence(s):
    newstring = s
    for i in range(len(s)):
        if s[i] in string.punctuation:
            newstring = newstring.replace(s[i], "")
        elif s[i] == " ":
            newstring = newstring.replace(s[i], "")
    newstring = newstring.lower()
    if newstring == newstring[::-1]:
        return True
    else:
        return False