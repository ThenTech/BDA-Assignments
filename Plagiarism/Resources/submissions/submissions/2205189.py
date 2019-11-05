import string


def is_palindrome_sentence(s):
    newstring = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] in string.ascii_lowercase:
            newstring += s[i]
    if newstring == newstring[::-1]:
        return True
    else:
        return False