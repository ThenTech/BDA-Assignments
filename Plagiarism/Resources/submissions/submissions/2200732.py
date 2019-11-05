def omdraaien(string):
    x = ""
    for i in range(len(string)):
        x += string[len(string) - i - 1]
    return x.upper()

def is_palindrome_sentence(string):
    verboden_tekens = [" ", ",", "?", ".", ";", ":", "/", "”", "’", "“","!"]
    string1 = ""
    for letter in string:
        if letter not in verboden_tekens:
            string1 = string1 + letter
    string1 = string1.upper()

    if string1 == omdraaien(string1):
        return True
    else:
        return False
pass
