import string


def cleanup_spaces(s):
    check = False
    for x in s:
        if x in string.ascii_letters:
            check = True
    sentence = ""
    if check:
        for letter in s:
            if letter != " " or sentence[len(sentence) - 1:] != " ":
                sentence += letter
        while sentence[0] == " ":
            sentence = sentence[1:]
        while sentence[len(sentence) - 1] == " ":
            sentence = sentence[:len(sentence) - 1]
    return sentence